# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectTask(HttpSavepointCase):
    """Tour tests for the ``project.task`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the stages, project and task used by the tours."""
        super().setUpClass()
        # user_id is explicit: cls.env runs as SUPERUSER and the record rules
        # would otherwise hide these fixtures from the tour's admin session.
        cls.admin = cls.env.ref("base.user_admin")
        Stage = cls.env["project.task.type"]
        cls.stage_a = Stage.create(
            {"name": "TOUR-TASK-STAGE-A", "sequence": 1, "state": "draft"}
        )
        cls.stage_b = Stage.create(
            {"name": "TOUR-TASK-STAGE-B", "sequence": 2, "state": "open"}
        )
        cls.project = cls.env["project.project"].create(
            {
                "name": "TOUR-TASK-PROJECT",
                "user_id": cls.admin.id,
                "type_ids": [(6, 0, [cls.stage_a.id, cls.stage_b.id])],
            }
        )
        cls.task_change = cls.env["project.task"].create(
            {
                "name": "TOUR-TASK-CHANGE",
                "project_id": cls.project.id,
                "stage_id": cls.stage_a.id,
                "user_id": cls.admin.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``project.task``.

        The conditional **Assign to Me** step is not clicked because the
        assignee defaults to the current user.

        IK: docs/project_task/01-create.md
        """
        self.start_tour("/web", "ssi_project_project_task_create", login="admin")

    def test_change_stage(self):
        """Run the change stage tour for ``project.task``.

        IK: docs/project_task/15-change-stage.md
        """
        self.start_tour("/web", "ssi_project_project_task_change_stage", login="admin")
