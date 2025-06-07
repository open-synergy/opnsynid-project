# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectDeliverable(models.Model):
    _name = "project_deliverable"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Project Milestone"

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        required=True,
    )
    ttype = fields.Selection(
        string="Group/Single?",
        selection=[
            ("group", "Group of Deliverable"),
            ("single", "Single Deliverable"),
        ],
        required=True,
        default="group",
    )
    allowed_parent_ids = fields.Many2many(
        string="Allowed Parent Deliverable",
        comodel_name="project_deliverable",
        compute="_compute_allowed_parent_ids",
        store=False,
        compute_sudo=True,
    )
    parent_id = fields.Many2one(
        string="Parent Milestone",
        comodel_name="project_deliverable",
    )

    # Child deliverable
    child_ids = fields.One2many(
        string="Child Deliverables",
        comodel_name="project_deliverable",
        inverse_name="parent_id",
    )
    number_of_child = fields.Integer(
        string="Num. of Child Deliverables",
        compute="_compute_number_of_child_deliverable",
        store=True,
        compute_sudo=True,
    )
    number_of_child_done = fields.Integer(
        string="Num. of Child Deliverables Done",
        compute="_compute_number_of_child_deliverable",
        store=True,
        compute_sudo=True,
    )
    child_completion_percentage = fields.Float(
        string="Child Deliverables Completion Percentage",
        compute="_compute_child_deliverable_completion_percentage",
        store=True,
        compute_sudo=True,
    )

    # Tasks
    task_ids = fields.One2many(
        string="Tasks",
        comodel_name="project.task",
        inverse_name="deliverable_id",
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

    completion_percentage = fields.Float(
        string="Completion Percentage",
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )

    @api.depends(
        "task_ids",
        "task_ids.deliverable_id",
        "task_ids.state",
    )
    def _compute_number_of_task(self):
        Task = self.env["project.task"]
        for record in self:
            all = done = 0
            criteria = [
                ("deliverable_id", "=", record.id),
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
                result = 1.0
            record.task_completion_percentage = result

    @api.depends(
        "child_ids",
        "child_ids.completion_percentage",
    )
    def _compute_number_of_child_deliverable(self):
        Deliverable = self.env["project_deliverable"]
        for record in self:
            all = done = 0
            criteria = [
                ("parent_id", "=", record.id),
            ]
            all = Deliverable.search_count(criteria)
            criteria += [
                ("completion_percentage", "=", 1.0),
            ]
            done = Deliverable.search_count(criteria)
            record.number_of_child = all
            record.number_of_child_done = done

    @api.depends(
        "number_of_child",
        "number_of_child_done",
    )
    def _compute_child_deliverable_completion_percentage(self):
        for record in self:
            result = 0.0
            try:
                result = record.number_of_child_done / record.number_of_child
            except ZeroDivisionError:
                result = 1.0
            record.child_completion_percentage = result

    @api.depends(
        "child_completion_percentage",
        "task_completion_percentage",
        "ttype",
    )
    def _compute_completion_percentage(self):
        for record in self:
            if record.ttype == "group":
                result = record.child_completion_percentage
            else:
                result = record.task_completion_percentage
            record.completion_percentage = result

    @api.depends(
        "project_id",
    )
    def _compute_allowed_parent_ids(self):
        Deliverable = self.env["project_deliverable"]
        for record in self:
            result = []
            if record.project_id:
                criteria = [("project_id", "=", record.project_id.id)]
                result = Deliverable.search(criteria).ids
            record.allowed_parent_ids = result

    @api.onchange(
        "project_id",
        "ttype",
    )
    def onchange_parent_id(self):
        self.parent_id = False
