# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class ProjectBatchAssignment(models.Model):
    _name = "project.batch_assignment"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_terminate",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
        "mixin.date_duration",
    ]
    _description = "Project Batch Assignment"
    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_open_button = False
    _automatically_insert_open_policy_fields = False

    # Mixin duration attribute
    _date_start_readonly = True
    _date_end_readonly = True
    _date_start_states_list = ["draft"]
    _date_start_states_readonly = ["draft"]
    _date_end_states_list = ["draft"]
    _date_end_states_readonly = ["draft"]

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

    date_assign = fields.Date(
        string="Date Assign",
        required=True,
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
    )

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        required=True,
        ondelete="cascade",
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
    )
    assignee_ids = fields.One2many(
        string="Assignees",
        comodel_name="project.batch_assignment_assignee",
        inverse_name="batch_id",
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
    )

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "done_ok",
            "open_ok",
            "terminate_ok",
            "cancel_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    def action_confirm(self):
        _super = super()
        _super.action_confirm()

        for record in self.sudo():
            record._create_project_assignment()
            record._update_project_assignment()
            record._confirm_project_assignment()

    def action_open(self):
        _super = super()
        _super.action_open()

        for record in self.sudo():
            record._open_project_assignment()

    def action_done(self):
        _super = super()
        _super.action_done()

        for record in self.sudo():
            record._done_project_assignment()

    def action_restart(self):
        _super = super()
        _super.action_restart()

        for record in self.sudo():
            record._restart_project_assignment()

    def action_cancel(self, cancel_reason=False):
        _super = super()
        _super.action_cancel(cancel_reason=cancel_reason)

        for record in self.sudo():
            record._cancel_project_assignment(cancel_reason=cancel_reason)

    def action_terminate(self, terminate_reason=False):
        _super = super()
        _super.action_terminate(terminate_reason=terminate_reason)

        for record in self.sudo():
            record._terminate_project_assignment(terminate_reason=terminate_reason)

    def _create_project_assignment(self):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._create_project_assignment()

    def _update_project_assignment(self):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._update_project_assignment()

    def _confirm_project_assignment(self):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._confirm_project_assignment()

    def _open_project_assignment(self):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._open_project_assignment()

    def _done_project_assignment(self):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._done_project_assignment()

    def _restart_project_assignment(self):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._restart_project_assignment()

    def _cancel_project_assignment(self, cancel_reason=False):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._cancel_project_assignment(cancel_reason=cancel_reason)

    def _terminate_project_assignment(self, terminate_reason=False):
        self.ensure_one()
        for assignee in self.assignee_ids:
            assignee._terminate_project_assignment(terminate_reason=terminate_reason)

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
