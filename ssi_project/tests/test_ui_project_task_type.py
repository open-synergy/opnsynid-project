# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectTaskType(HttpSavepointCase):
    """Tour tests for the ``project.task.type`` work instructions."""

    def test_create(self):
        """Run the create tour for ``project.task.type``.

        IK: docs/project_task_type/01-create.md
        """
        self.start_tour("/web", "ssi_project_project_task_type_create", login="admin")
