# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, Warning as UserError


class TaskDependency(models.Model):
    _name = "task.dependency"
    _description = "Task Dependency"

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
        required=True,
        ondelete="cascade",
    )
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        required=True,
        ondelete="restrict",
    )
    predecessor_task_id = fields.Many2one(
        string="Predecessor Task",
        comodel_name="project.task",
        required=True,
        ondelete="restrict",
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
    task_stage_id = fields.Many2one(
        string="Task Stage",
        comodel_name="project.task.type",
        related="task_id.stage_id",
        store=False,
        readonly=False,
    )
    predecessor_task_stage_id = fields.Many2one(
        string="Predecessor Task Stage",
        comodel_name="project.task.type",
        related="predecessor_task_id.stage_id",
        store=False,
        readonly=False,
    )
    task_state = fields.Selection(
        string="Task State",
        related="task_id.state",
        store=True,
        readonly=False,
    )
    predecessor_task_state = fields.Selection(
        string="Predecessor Task State",
        related="predecessor_task_id.state",
        store=True,
        readonly=False,
    )

    @api.constrains(
        "task_id",
        "predecessor_task_id",
    )
    def check_no_same_task(self):
        if self.task_id == self.predecessor_task_id:
            raise ValidationError(
                _("You can not select itself for predecessor/sucessor")
            )

    # task T/10/23/004552
    @api.constrains("predecessor_task_id")
    def _check_predecessor_task_id(self):
        for record in self:
            checks = self.env["task.dependency"].search(
                [
                    ("id", "!=", record.id),
                    ("predecessor_task_id", "=", record.predecessor_task_id.id),
                    ("task_id", "=", record.task_id.id),
                ]
            )
            if checks:
                error_message = _(
                    """
                Context: Create/update task
                Database ID: %s
                Problem: Predecessor task: %s is used
                Solution: Use another predecessor task
                """
                    % (
                        record.task_id.id,
                        record.predecessor_task_id.name,
                    )
                )
                raise UserError(error_message)
