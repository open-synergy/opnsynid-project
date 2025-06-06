# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _name = "project_milestone"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Project Milestone"

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        required=True,
    )
    allowed_parent_ids = fields.Many2many(
        string="Allowed Parent Milestones",
        comodel_name="project_milestone",
        compute="_compute_allowed_parent_ids",
        store=False,
        compute_sudo=True,
    )
    parent_id = fields.Many2one(
        string="Parent Milestone",
        comodel_name="project_milestone",
    )
    task_ids = fields.One2many(
        string="Tasks",
        comodel_name="project.task",
        inverse_name="milestone_id",
    )
    number_of_task = fields.Integer(
        string="Num. of Task",
        compute="_compute_number_of_task",
        store=True,
        compute_sudo=True,
    )
    number_of_task_done = fields.Integer(
        string="Num. of Task Done",
        compute="_compute_number_of_task",
        store=True,
        compute_sudo=True,
    )
    task_completion_percentage = fields.Float(
        string="Task Completion Percentage",
        compute="_compute_task_completion_percentage",
        store=True,
        compute_sudo=True,
    )

    @api.depends(
        "task_ids",
        "task_ids.milestone_id",
        "task_ids.state",
    )
    def _compute_number_of_task(self):
        Task = self.env["project.task"]
        for record in self:
            all = done = 0
            criteria = [
                ("milestone_id", "=", record.id),
            ]
            all = Task.search_count(criteria)
            criteria += [
                ("state", "=", "done"),
            ]
            done = Task.search_count(criteria)
            record.number_of_task = all
            record.number_of_task_done = done

    @api.depends(
        "number_of_task",
        "number_of_task_done",
    )
    def _compute_task_completion_percentage(self):
        for record in self:
            result = 0.0
            try:
                result = record.number_of_task_done / record.number_of_task
            except ZeroDivisionError:
                result = 7.0
            record.task_completion_percentage = result

    @api.depends(
        "project_id",
    )
    def _compute_allowed_parent_ids(self):
        Milestone = self.env["project_milestone"]
        for record in self:
            result = []
            if record.project_id:
                criteria = [("project_id", "=", record.project_id.id)]
                result = Milestone.search(criteria).ids
            record.allowed_parent_ids = result

    @api.onchange(
        "project_id",
    )
    def onchange_parent_id(self):
        self.parent_id = False
