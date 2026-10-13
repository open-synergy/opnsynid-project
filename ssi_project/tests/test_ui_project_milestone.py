# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectMilestone(HttpSavepointCase):
    """Tour tests for the ``project_milestone`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the projects, phase and milestones used by the tours."""
        super().setUpClass()
        # user_id is explicit: cls.env runs as SUPERUSER and the record rules
        # would otherwise hide these fixtures from the tour's admin session.
        cls.admin = cls.env.ref("base.user_admin")
        Project = cls.env["project.project"]
        Milestone = cls.env["project_milestone"]
        cls.project = Project.create(
            {"name": "TOUR-MS-PROJECT", "user_id": cls.admin.id}
        )
        cls.phase = cls.env["project_phase"].create(
            {
                "name": "TOUR-MS-PHASE",
                "title": "TOUR-MS-PHASE",
                "ttype": "single",
                "project_id": cls.project.id,
                "date_due": "2026-12-31",
                "user_id": cls.admin.id,
            }
        )
        cls.project_edit = Project.create(
            {"name": "TOUR-MSE-PROJECT", "user_id": cls.admin.id}
        )
        cls.milestone_edit = Milestone.create(
            {
                "name": "TOUR-MS-EDIT",
                "project_id": cls.project_edit.id,
                "user_id": cls.admin.id,
            }
        )
        cls.project_delete = Project.create(
            {"name": "TOUR-MSD-PROJECT", "user_id": cls.admin.id}
        )
        cls.milestone_delete = Milestone.create(
            {
                "project_id": cls.project_delete.id,
                "user_id": cls.admin.id,
            }
        )

        # Pre-Conditions for 04-confirm / 05-approve / 09-finish / 10-cancel.
        # The approval chain runs through action methods as the admin user
        # with a cache flush in between (T-04), never through write().
        cls.project_flow = Project.create(
            {"name": "TOUR-MSF-PROJECT", "user_id": cls.admin.id}
        )

        def _milestone(name):
            """Create a draft milestone owned by the tour user.

            :param name: unique milestone name
            :return: the created milestone
            """
            return Milestone.create(
                {
                    "name": name,
                    "project_id": cls.project_flow.id,
                    "user_id": cls.admin.id,
                }
            )

        cls.milestone_confirm = _milestone("TOUR-MS-CONFIRM")
        cls.milestone_cancel = _milestone("TOUR-MS-CANCEL")
        cls.milestone_approve = _milestone("TOUR-MS-APPROVE")
        cls.milestone_approve.with_user(cls.admin).action_confirm()
        cls.milestone_approve.invalidate_cache()
        cls.milestone_finish = _milestone("TOUR-MS-FINISH")
        cls.milestone_finish.with_user(cls.admin).action_confirm()
        cls.milestone_finish.invalidate_cache()
        cls.milestone_finish.with_user(cls.admin).action_approve_approval()
        cls.milestone_finish.invalidate_cache()
        cls.env["base.cancel_reason"].create(
            {
                "name": "Tour Milestone Cancel Reason",
                "code": "TOURMSCR",
                # Only reasons in ir.model.all_cancel_reason_ids reach the
                # wizard radio; global_use=True puts this one there.
                "global_use": True,
            }
        )

    def test_create(self):
        """Run the create tour for ``project_milestone``.

        IK: docs/project_milestone/01-create.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``project_milestone``.

        IK: docs/project_milestone/02-edit.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``project_milestone``.

        IK: docs/project_milestone/03-delete.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_delete", login="admin")

    def test_confirm(self):
        """Run the confirm tour for ``project_milestone``.

        IK: docs/project_milestone/04-confirm.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_confirm", login="admin")

    def test_approve(self):
        """Run the approve tour for ``project_milestone``.

        IK: docs/project_milestone/05-approve.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_approve", login="admin")

    def test_finish(self):
        """Run the finish tour for ``project_milestone``.

        IK: docs/project_milestone/09-finish.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_finish", login="admin")

    def test_cancel(self):
        """Run the cancel tour for ``project_milestone``.

        IK: docs/project_milestone/10-cancel.md
        """
        self.start_tour("/web", "ssi_project_project_milestone_cancel", login="admin")
