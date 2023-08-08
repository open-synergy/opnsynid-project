# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class TaskTemplate(models.Model):
    _name = "task.template"
    _inherit = [
        "task.template",
    ]

    def _get_user(self, project):
        self.ensure_one()
        _super = super(TaskTemplate, self)
        result = _super._get_user(project)
        ProjectAssignment = self.env["project.assignment"]
        if self.type_id and self.type_id.role_id:
            criteria = [
                ("role_id", "=", self.type_id.role_id.id),
                ("project_id", "=", project.id),
                ("id", "in", project.active_assignment_ids.ids),
            ]
            assignments = ProjectAssignment.search(criteria)
            if len(assignments) == 1:
                result = assignments[0].asignee_id
        return result

    def _prepare_task_creation(self, project):
        self.ensure_one()
        _super = super(TaskTemplate, self)
        result = _super._prepare_task_creation(project)
        role = self.type_id and self.type_id.role_id or False
        result.update(
            {
                "role_id": role and role.id or False,
            }
        )
        return result
