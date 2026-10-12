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
