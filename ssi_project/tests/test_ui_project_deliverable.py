# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectDeliverable(HttpSavepointCase):
    """Tour tests for the ``project_deliverable`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the projects, type data and deliverables used by the tours."""
        super().setUpClass()
        # user_id is explicit: cls.env runs as SUPERUSER and the record rules
        # would otherwise hide these fixtures from the tour's admin session.
        cls.admin = cls.env.ref("base.user_admin")
        Project = cls.env["project.project"]
        Deliverable = cls.env["project_deliverable"]
        cls.project_new = Project.create(
            {"name": "TOURDL-NEWPROJECT", "user_id": cls.admin.id}
        )
        cls.project_flow = Project.create(
            {"name": "TOURDL-FLOWPROJECT", "user_id": cls.admin.id}
        )
        cls.category = cls.env["project_deliverable_type_category"].create(
            {"name": "TOURDL-CATEGORY", "code": "TOURDLCAT"}
        )
        cls.type = cls.env["project_deliverable_type"].create(
            {
                "name": "TOURDL-TYPE",
                "code": "TOURDLTYPE",
                "category_id": cls.category.id,
            }
        )

        def _deliverable(title):
            """Create a draft single deliverable owned by the tour user.

            :param title: unique deliverable title
            :return: the created deliverable
            """
            return Deliverable.create(
                {
                    "title": title,
                    "ttype": "single",
                    "project_id": cls.project_flow.id,
                    "category_id": cls.category.id,
                    "type_id": cls.type.id,
                    "date": "2026-01-01",
                    "date_due": "2026-12-31",
                    "user_id": cls.admin.id,
                }
            )

        # Pre-Conditions for 04-confirm / 05-approve / 09-finish / 10-cancel.
        # The approval chain runs through action methods as the admin user
        # with a cache flush in between (T-04), never through write().
        cls.deliverable_confirm = _deliverable("TOURDL-CONFIRM")
        cls.deliverable_cancel = _deliverable("TOURDL-CANCEL")
        cls.deliverable_approve = _deliverable("TOURDL-APPROVE")
        cls.deliverable_approve.with_user(cls.admin).action_confirm()
        cls.deliverable_approve.invalidate_cache()
        cls.deliverable_finish = _deliverable("TOURDL-FINISH")
        cls.deliverable_finish.with_user(cls.admin).action_confirm()
        cls.deliverable_finish.invalidate_cache()
        cls.deliverable_finish.with_user(cls.admin).action_approve_approval()
        cls.deliverable_finish.invalidate_cache()
        cls.env["base.cancel_reason"].create(
            {
                "name": "Tour Deliverable Cancel Reason",
                "code": "TOURDLCR",
                # Only reasons in ir.model.all_cancel_reason_ids reach the
                # wizard radio; global_use=True puts this one there.
                "global_use": True,
            }
        )

    def test_create(self):
        """Run the create tour for ``project_deliverable``.

        IK: docs/project_deliverable/01-create.md
        """
        self.start_tour("/web", "ssi_project_project_deliverable_create", login="admin")

    def test_confirm(self):
        """Run the confirm tour for ``project_deliverable``.

        IK: docs/project_deliverable/04-confirm.md
        """
        self.start_tour(
            "/web", "ssi_project_project_deliverable_confirm", login="admin"
        )

    def test_approve(self):
        """Run the approve tour for ``project_deliverable``.

        IK: docs/project_deliverable/05-approve.md
        """
        self.start_tour(
            "/web", "ssi_project_project_deliverable_approve", login="admin"
        )

    def test_finish(self):
        """Run the finish tour for ``project_deliverable``.

        IK: docs/project_deliverable/09-finish.md
        """
        self.start_tour("/web", "ssi_project_project_deliverable_finish", login="admin")

    def test_cancel(self):
        """Run the cancel tour for ``project_deliverable``.

        IK: docs/project_deliverable/10-cancel.md
        """
        self.start_tour("/web", "ssi_project_project_deliverable_cancel", login="admin")
