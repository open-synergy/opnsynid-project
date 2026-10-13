# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectProject(HttpSavepointCase):
    """Tour tests for the ``project.project`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the unit partner and one project per tour state."""
        super().setUpClass()
        # user_id is explicit: cls.env runs as SUPERUSER and the record rule
        # would otherwise hide these fixtures from the tour's admin session.
        cls.admin = cls.env.ref("base.user_admin")
        cls.unit = cls.env["res.partner"].create(
            {"name": "TOUR-UNIT-ORG", "is_company": True}
        )
        Project = cls.env["project.project"]

        def _project(name):
            """Create a draft project owned by the tour user.

            :param name: unique project name
            :return: the created project
            """
            return Project.create({"name": name, "user_id": cls.admin.id})

        cls.project_start = _project("TOUR-PRJ-START")
        cls.project_pending = _project("TOUR-PRJ-PENDING")
        cls.project_pending.action_confirm()
        cls.project_finish = _project("TOUR-PRJ-FINISH")
        cls.project_finish.action_confirm()
        cls.project_cancel = _project("TOUR-PRJ-CANCEL")
        cls.project_restart = _project("TOUR-PRJ-RESTART")
        cls.project_restart.action_cancel()

    def test_create(self):
        """Run the create tour for ``project.project``.

        IK: docs/project_project/01-create.md
        """
        self.start_tour("/web", "ssi_project_project_project_create", login="admin")

    def test_start(self):
        """Run the start tour for ``project.project``.

        IK: docs/project_project/07-start.md
        """
        self.start_tour("/web", "ssi_project_project_project_start", login="admin")

    def test_pending(self):
        """Run the pending tour for ``project.project``.

        IK: docs/project_project/15-pending.md
        """
        self.start_tour("/web", "ssi_project_project_project_pending", login="admin")

    def test_finish(self):
        """Run the finish tour for ``project.project``.

        IK: docs/project_project/09-finish.md
        """
        self.start_tour("/web", "ssi_project_project_project_finish", login="admin")

    def test_cancel(self):
        """Run the cancel tour for ``project.project``.

        IK: docs/project_project/10-cancel.md
        """
        self.start_tour("/web", "ssi_project_project_project_cancel", login="admin")

    def test_restart(self):
        """Run the restart tour for ``project.project``.

        IK: docs/project_project/12-restart.md
        """
        self.start_tour("/web", "ssi_project_project_project_restart", login="admin")
