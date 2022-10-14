# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class TaskTemplate(models.Model):
    _name = "task.template"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Task Template"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="task.type",
    )
    user_id = fields.Many2one(
        string="Assigned To",
        comodel_name="res.users",
    )

    def _create_task(self, project):
        self.ensure_one()
        Task = self.env["project.task"]
        Task.create(self._prepare_task_creation(project))

    def _prepare_task_creation(self, project):
        self.ensure_one()
        return {
            "name": self.name,
            "type_id": self.type_id and self.type_id.id or False,
            "user_id": self.user_id and self.user_id.id or False,
            "project_id": project.id,
            "template_id": self.id,
        }
