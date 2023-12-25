# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


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
    description = fields.Html(
        string="Description",
    )
    baseline_method = fields.Selection(
        string="Baseline Method",
        selection=[
            ("none", "None"),
            ("project", "Project"),
            ("task", "Task"),
        ],
        required=True,
        default="none",
    )
    baseline_task_template_id = fields.Many2one(
        string="Baseline Task Template",
        comodel_name="task.template",
    )
    baseline_offset = fields.Integer(
        string="Baseline Offset",
        default=0,
    )

    @api.onchange(
        "baseline_method",
    )
    def onchange_baseline_task_template_id(self):
        self.baseline_task_template_id = False

    def _create_task(self, project):
        self.ensure_one()
        Task = self.env["project.task"]
        Task.create(self._prepare_task_creation(project))

    def _get_user(self, project):
        self.ensure_one()
        return self.user_id

    def _prepare_task_creation(self, project):
        self.ensure_one()
        user = self._get_user(project)
        return {
            "name": self.name,
            "type_id": self.type_id and self.type_id.id or False,
            "user_id": user and user.id or False,
            "project_id": project.id,
            "template_id": self.id,
            "description": self.description,
        }
