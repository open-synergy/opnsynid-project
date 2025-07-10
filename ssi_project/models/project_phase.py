# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date as datetime_date

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class ProjectPhase(models.Model):
    _name = "project_phase"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_terminate",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
        "mixin.transaction_date_due",
    ]
    _description = "Project Phase"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_open_button = False
    _automatically_insert_open_policy_fields = False

    # Attributes related to add element on form view automatically
    _automatically_insert_multiple_approval_page = True
    _statusbar_visible_label = "draft,confirm,open"
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

    title = fields.Char(
        string="Title",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
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
    ttype = fields.Selection(
        string="Group/Single?",
        selection=[
            ("group", "Group of Phase"),
            ("single", "Single Phase"),
        ],
        required=True,
        default="group",
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
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    allowed_parent_ids = fields.Many2many(
        string="Allowed Parent Deliverable",
        comodel_name="project_phase",
        compute="_compute_allowed_parent_ids",
        store=False,
        compute_sudo=True,
    )
    parent_id = fields.Many2one(
        string="Parent Phase",
        comodel_name="project_phase",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    # Child deliverable
    child_ids = fields.One2many(
        string="Child Phases",
        comodel_name="project_phase",
        inverse_name="parent_id",
    )
    number_of_child = fields.Integer(
        string="Num. of Child Phases",
        compute="_compute_number_of_child",
        store=True,
        compute_sudo=True,
    )
    number_of_child_done = fields.Integer(
        string="Num. of Child Phases Done",
        compute="_compute_number_of_child",
        store=True,
        compute_sudo=True,
    )
    child_completion_percentage = fields.Float(
        string="Child Phases Completion Percentage",
        compute="_compute_child_completion_percentage",
        store=True,
        compute_sudo=True,
    )

    # Tasks
    task_ids = fields.One2many(
        string="Tasks",
        comodel_name="project.task",
        inverse_name="phase_id",
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

    # Deliverable
    deliverable_ids = fields.One2many(
        string="Deliverables",
        comodel_name="project_deliverable",
        inverse_name="phase_id",
    )
    number_of_deliverable = fields.Integer(
        string="Num. of Deliverables",
        compute="_compute_number_of_deliverable",
        store=True,
        compute_sudo=True,
    )
    number_of_deliverable_done = fields.Integer(
        string="Num. of Deliverable Done",
        compute="_compute_number_of_deliverable",
        store=True,
        compute_sudo=True,
    )
    deliverable_completion_percentage = fields.Float(
        string="Deliverable Completion Percentage",
        compute="_compute_deliverable_completion_percentage",
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
        "task_ids.phase_id",
        "task_ids.stage_id",
    )
    def _compute_number_of_task(self):
        Task = self.env["project.task"]
        for record in self:
            all_task = done_task = 0
            criteria = [
                ("phase_id", "=", record.id),
            ]
            all_task = Task.search_count(criteria)
            criteria += [
                ("state", "=", "done"),
            ]
            done_task = Task.search_count(criteria)
            record.number_of_task = all_task
            record.number_of_task_done = done_task

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
                result = 0.0
            record.task_completion_percentage = result

    @api.depends(
        "child_ids",
        "child_ids.completion_percentage",
        "child_ids.state",
        "child_ids.parent_id",
    )
    def _compute_number_of_child(self):
        Phase = self.env["project_phase"]
        for record in self:
            all_child = done_child = 0
            criteria = [
                ("parent_id", "=", record.id),
                ("state", "in", ["open", "done"]),
            ]
            all_child = Phase.search_count(criteria)
            criteria += [
                ("completion_percentage", "=", 1.0),
            ]
            done_child = Phase.search_count(criteria)
            record.number_of_child = all_child
            record.number_of_child_done = done_child

    @api.depends(
        "number_of_child",
        "number_of_child_done",
    )
    def _compute_child_completion_percentage(self):
        for record in self:
            result = 0.0
            try:
                result = record.number_of_child_done / record.number_of_child
            except ZeroDivisionError:
                result = 0.0
            record.child_completion_percentage = result

    @api.depends(
        "deliverable_ids",
        "deliverable_ids.state",
        "deliverable_ids.phase_id",
    )
    def _compute_number_of_deliverable(self):
        Deliverable = self.env["project_deliverable"]
        for record in self:
            all_child = done_child = 0
            criteria = [
                ("phase_id", "=", record.id),
                ("state", "in", ["open", "done"]),
            ]
            all_child = Deliverable.search_count(criteria)
            criteria = [
                ("phase_id", "=", record.id),
                ("state", "=", "done"),
            ]
            done_child = Deliverable.search_count(criteria)
            record.number_of_child = all_child
            record.number_of_child_done = done_child

    @api.depends(
        "number_of_deliverable",
        "number_of_deliverable_done",
    )
    def _compute_deliverable_completion_percentage(self):
        for record in self:
            result = 0.0
            try:
                result = (
                    record.number_of_deliverable_done / record.number_of_deliverable
                )
            except ZeroDivisionError:
                result = 0.0
            record.deliverable_completion_percentage = result

    @api.depends(
        "child_completion_percentage",
        "task_completion_percentage",
        "ttype",
        "number_of_child",
        "number_of_child_done",
        "number_of_task",
        "number_of_task_done",
        "child_ids",
        "child_ids.completion_percentage",
        "child_ids.state",
        "child_ids.parent_id",
        "task_ids",
        "task_ids.phase_id",
        "task_ids.stage_id",
        "task_ids.stage_id",
        "deliverable_ids",
        "deliverable_ids.state",
        "deliverable_ids.phase_id",
    )
    def _compute_completion_percentage(self):
        for record in self:
            if record.ttype == "group":
                result = record.child_completion_percentage
            else:
                result = (
                    record.task_completion_percentage
                    + record.deliverable_completion_percentage
                ) / 2.0
            record.completion_percentage = result

    @api.depends(
        "project_id",
    )
    def _compute_allowed_parent_ids(self):
        Deliverable = self.env["project_phase"]
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

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
