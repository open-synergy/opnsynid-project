# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class CustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if "project_assignment_count" in counters:
            values["project_assignment_count"] = (
                request.env["project.assignment"].search_count([])
                if request.env["project.assignment"].check_access_rights(
                    "read", raise_exception=False
                )
                else 0
            )
        return values

    def _project_assignment_get_page_view_values(
        self, project_assignment, access_token, **kwargs
    ):
        values = {
            "page_name": "project-assignments",
            "project_assignment": project_assignment,
        }
        return self._get_page_view_values(
            project_assignment,
            access_token,
            values,
            "my_project_assignments_history",
            False,
            **kwargs,
        )

    @http.route(
        ["/my/project-assignments", "/my/project-assignments/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_project_assignments(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        values = self._prepare_portal_layout_values()
        Assignment = request.env["project.assignment"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("# Assignment"), "order": "name"},
        }
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]

        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]

        # projects count
        project_assignment_count = Assignment.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/project-assignments",
            url_args={"date_begin": date_begin, "date_end": date_end, "sortby": sortby},
            total=project_assignment_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        project_assignments = Assignment.search(
            domain, order=order, limit=self._items_per_page, offset=pager["offset"]
        )
        request.session["my_project_assignments_history"] = project_assignments.ids[
            :100
        ]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "project_assignments": project_assignments,
                "page_name": "project-assignments",
                "default_url": "/my/project-assignments",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "sortby": sortby,
            }
        )
        return request.render(
            "ssi_project_assignment.portal_my_project_assignments", values
        )

    @http.route(
        ["/my/project-assignment/<int:assignment_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_project_assignment(self, assignment_id=None, access_token=None, **kw):
        try:
            project_assignment_sudo = self._document_check_access(
                "project.assignment", assignment_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._project_assignment_get_page_view_values(
            project_assignment_sudo, access_token, **kw
        )
        user_assignment_id = request.env["project.assignment"].search(
            [
                ("id", "=", assignment_id),
            ]
        )
        values.update(
            {
                "access_token": values.get(
                    "access_token", user_assignment_id.access_token
                ),
                "approve_ok": user_assignment_id.approve_ok,
                "reject_ok": user_assignment_id.reject_ok,
            }
        )
        return request.render(
            "ssi_project_assignment.portal_my_project_assignment", values
        )

    @http.route(
        ["/my/project-assignment/<int:assignment_id>/approve"],
        type="http",
        auth="public",
        website=True,
    )
    def approve(self, assignment_id, access_token=None, **post):
        try:
            user_assignment_id = request.env["project.assignment"].search(
                [
                    ("id", "=", assignment_id),
                ]
            )
        except (AccessError, MissingError):
            return request.redirect("/my")
        user_assignment_id.action_approve_approval()
        return request.redirect(f"/my/project-assignment/{assignment_id}")

    @http.route(
        ["/my/project-assignment/<int:assignment_id>/reject"],
        type="http",
        auth="public",
        website=True,
    )
    def reject(self, assignment_id, access_token=None, **post):
        try:
            user_assignment_id = request.env["project.assignment"].search(
                [
                    ("id", "=", assignment_id),
                ]
            )
        except (AccessError, MissingError):
            return request.redirect("/my")
        user_assignment_id.action_reject_approval()
        return request.redirect(f"/my/project-assignment/{assignment_id}")
