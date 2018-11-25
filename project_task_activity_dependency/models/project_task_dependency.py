# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields, _
from openerp.exceptions import Warning as UserError


class ProjectTaskDependency(models.Model):
    _name = "project.task_dependency"
    _descrption = "Project Task Dependency"

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
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
        selection=[
            ("draft", "New"),
            ("open", "In Progress"),
            ("pending", "Pending"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        related="task_id.state",
        store=False,
        readonly=False,
    )
    predecessor_task_state = fields.Selection(
        string="Predecessor Task State",
        selection=[
            ("draft", "New"),
            ("open", "In Progress"),
            ("pending", "Pending"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        related="predecessor_task_id.state",
        store=False,
        readonly=False,
    )

    @api.constrains(
        "task_id",
        "predecessor_task_id",
    )
    def check_no_same_task(self):
        if self.task_id == self.predecessor_task_id:
            raise UserError(
                _("You can not select itself for predecessor/sucessor"))
