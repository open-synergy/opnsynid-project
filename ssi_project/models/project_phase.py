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
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )
    number_of_child_done = fields.Integer(
        string="Num. of Child Phases Done",
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )
    child_completion_percentage = fields.Float(
        string="Child Phases Completion Percentage",
        compute="_compute_completion_percentage",
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
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )
    number_of_task_done = fields.Integer(
        string="Num. of Task Done",
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )
    task_completion_percentage = fields.Float(
        string="Task Completion Percentage",
        compute="_compute_completion_percentage",
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
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )
    number_of_deliverable_done = fields.Integer(
        string="Num. of Deliverable Done",
        compute="_compute_completion_percentage",
        store=True,
        compute_sudo=True,
    )
    deliverable_completion_percentage = fields.Float(
        string="Deliverable Completion Percentage",
        compute="_compute_completion_percentage",
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
        "ttype",
        "task_ids",
        "task_ids.state",
        "task_ids.stage_id",
        "child_ids",
        "child_ids.state",
        "child_ids.completion_percentage",
        "deliverable_ids",
        "deliverable_ids.state",
    )
    def _compute_completion_percentage(self):
        """Compute the counters and percentages of tasks, children,
        deliverables and the overall completion percentage.

        All ten fields are filled in one pass because the base
        automations (open to done) read ``completion_percentage`` while
        the source group is still being computed; a separate compute
        would read stale source percentages. ``completion_percentage``
        is built from local variables, never from stored fields.

        * Tasks: all ``task_ids`` are counted; those with ``state`` equal
          to ``done`` are done.
        * Children: ``child_ids`` in state ``open`` or ``done`` are
          counted; those with ``completion_percentage`` equal to 1.0 are
          done.
        * Deliverables: ``deliverable_ids`` in state ``open`` or ``done``
          are counted; those in ``done`` are done.
        * Completion: the child percentage for a group phase, otherwise
          the mean of the task and deliverable percentages.

        :return: nothing; assigns ``number_of_task``,
            ``number_of_task_done``, ``task_completion_percentage``,
            ``number_of_child``, ``number_of_child_done``,
            ``child_completion_percentage``, ``number_of_deliverable``,
            ``number_of_deliverable_done``,
            ``deliverable_completion_percentage`` and
            ``completion_percentage``
        """
        for record in self:
            all_task = len(record.task_ids)
            done_task = len(record.task_ids.filtered(lambda t: t.state == "done"))
            task_result = 0.0
            if all_task:
                task_result = done_task / all_task

            valid_children = record.child_ids.filtered(
                lambda c: c.state in ["open", "done"]
            )
            all_child = len(valid_children)
            done_child = len(
                valid_children.filtered(lambda c: c.completion_percentage == 1.0)
            )
            child_result = 0.0
            if all_child:
                child_result = done_child / all_child

            valid_deliverables = record.deliverable_ids.filtered(
                lambda d: d.state in ["open", "done"]
            )
            all_deliverable = len(valid_deliverables)
            done_deliverable = len(
                valid_deliverables.filtered(lambda d: d.state == "done")
            )
            deliverable_result = 0.0
            if all_deliverable:
                deliverable_result = done_deliverable / all_deliverable

            if record.ttype == "group":
                result = child_result
            else:
                result = (task_result + deliverable_result) / 2.0

            record.number_of_task = all_task
            record.number_of_task_done = done_task
            record.task_completion_percentage = task_result
            record.number_of_child = all_child
            record.number_of_child_done = done_child
            record.child_completion_percentage = child_result
            record.number_of_deliverable = all_deliverable
            record.number_of_deliverable_done = done_deliverable
            record.deliverable_completion_percentage = deliverable_result
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
