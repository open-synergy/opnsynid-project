# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CreateSucessorTask(models.TransientModel):
    _name = "create_sucessor_task"
    _description = "Create Sucessor Tasks"

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
        required=True,
        default=lambda self: self._default_task_id(),
    )
    detail_ids = fields.One2many(
        string="Details",
        comodel_name="create_sucessor_task_detail",
        inverse_name="wizard_id",
    )

    @api.model
    def _default_task_id(self):
        return self.env.context.get("active_id", False)

    def action_confirm(self):
        for wizard in self.sudo():
            wizard._confirm()

    def _confirm(self):
        self.ensure_one()
        for detail in self.detail_ids:
            detail._create_task()


class CreateSucessorTaskDetail(models.TransientModel):
    _name = "create_sucessor_task_detail"
    _description = "Create Sucessor Tasks - Detail"

    wizard_id = fields.Many2one(
        string="Wizard",
        comodel_name="create_sucessor_task",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(
        string="Task Summary",
    )
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
    )
    user_id = fields.Many2one(
        string="Assigned To",
        comodel_name="res.users",
    )
    dependency_type = fields.Selection(
        string="Dependency Type",
        selection=[
            ("start_finish", "Start-To-Finish"),
            ("start_start", "Start-To-Start"),
            ("finish_start", "Finish-To-Start"),
            ("finish_finish", "Finish-To-Finish"),
        ],
        required=True,
    )

    def _create_task(self):
        self.ensure_one()
        Task = self.env["project.task"]
        data = self._prepare_task_creation_value()
        temp_record = Task.new(data)
        temp_record = self._compute_task_onchange(temp_record)
        values = temp_record._convert_to_write(temp_record._cache)
        Task.create(values)

    def _compute_task_onchange(self, task_cache):
        self.ensure_one()
        return task_cache

    def _prepare_task_creation_value(self):
        self.ensure_one()
        wizard = self.wizard_id
        return {
            "name": self.name or wizard.task_id.name,
            "project_id": self.project_id
            and self.project_id.id
            or wizard.task_id.project_id.id,
            "user_id": self.user_id and self.user_id.id or False,
            "predecessor_ids": [
                (
                    0,
                    0,
                    {
                        "project_id": wizard.task_id.project_id.id,
                        "predecessor_task_id": wizard.task_id.id,
                        "dependency_type": self.dependency_type,
                    },
                ),
            ],
        }
