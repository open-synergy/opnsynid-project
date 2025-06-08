# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date as datetime_date

from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _name = "project_milestone"
    _inherit = [
        "mixin.transaction_confirm",
        "mixin.transaction_cancel",
        "mixin.transaction_open",
        "mixin.transaction_done",
        "mixin.transaction_terminate",
    ]
    _description = "Project Milestone"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_open_button = False
    _automatically_insert_open_policy_fields = False
    _automatically_insert_done_button = False
    _automatically_insert_done_policy_fields = False

    # Attributes related to add element on form view automatically
    _automatically_insert_multiple_approval_page = True
    _statusbar_visible_label = "draft,confirm,open,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "done_ok",
        "cancel_ok",
        "terminate_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "action_done",
        "action_terminate",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_open",
        "dom_done",
        "dom_terminate",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "open"

    date = fields.Date(
        string="Date",
        default=lambda r: datetime_date.today(),
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
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

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "done_ok",
            "terminate_ok",
            "cancel_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res
