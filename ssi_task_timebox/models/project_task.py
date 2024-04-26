# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    @api.depends(
        "timebox_ids",
        "timebox_ids.date_start",
        "timebox_ids.date_end",
        "timebox_ids.state",
    )
    def _compute_timebox(self):
        for document in self:
            timebox_latest_id = (
                timebox_date_start
            ) = (
                timebox_date_end
            ) = (
                timebox_initial_id
            ) = (
                timebox_initial_date_start
            ) = (
                timebox_initial_date_end
            ) = (
                timebox_upcoming_id
            ) = (
                timebox_upcoming_date_start
            ) = timebox_upcoming_date_end = on_running_timebox = False
            if len(document.timebox_ids) > 0:
                timebox_latest_id = document.timebox_ids[-1]
                timebox_date_start = timebox_latest_id.date_start
                timebox_date_end = timebox_latest_id.date_end
                timebox_initial_id = document.timebox_ids[0]
                timebox_initial_date_start = timebox_initial_id.date_start
                timebox_initial_date_end = timebox_initial_id.date_end
            upcoming_timeboxes = document.timebox_ids.filtered(
                lambda r: r.state in ["new", "open"]
            )
            if len(upcoming_timeboxes) > 0:
                timebox_upcoming_id = upcoming_timeboxes[0]
                timebox_upcoming_date_start = timebox_upcoming_id.date_start
                timebox_upcoming_date_end = timebox_upcoming_id.date_end
            active_timeboxes = document.timebox_ids.filtered(
                lambda r: r.state == "open"
            )
            if len(active_timeboxes) == 1:
                on_running_timebox = True
            document.timebox_latest_id = timebox_latest_id
            document.timebox_date_start = timebox_date_start
            document.timebox_date_end = timebox_date_end
            document.timebox_initial_id = timebox_initial_id
            document.timebox_initial_date_start = timebox_initial_date_start
            document.timebox_initial_date_end = timebox_initial_date_end
            document.timebox_upcoming_id = timebox_upcoming_id
            document.timebox_upcoming_date_start = timebox_upcoming_date_start
            document.timebox_upcoming_date_end = timebox_upcoming_date_end
            document.on_running_timebox = on_running_timebox

    @api.depends("timebox_ids.state")
    def _compute_num_timebox(self):
        for rec in self:
            rec.num_of_draft_timebox = len(rec.timebox_ids.filtered(lambda t: t.state == 'new'))
            rec.num_of_done_timebox = len(rec.timebox_ids.filtered(lambda t: t.state == 'done'))

    timebox_ids = fields.Many2many(
        string="Timeboxes",
        comodel_name="task.timebox",
        relation="rel_timebox_2_task",
        column1="task_id",
        column2="timebox_id",
    )
    timebox_latest_id = fields.Many2one(
        string="Letest Timebox",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_date_start = fields.Date(
        string="Latest Timebox Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_date_end = fields.Date(
        string="Lates Timebox Date Stop",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_id = fields.Many2one(
        string="Timebox Initial",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_start = fields.Date(
        string="Timebox Initial Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_end = fields.Date(
        string="Timebox Initial Date Stop",
        compute="_compute_timebox",
        store=True,
    )
    timebox_upcoming_id = fields.Many2one(
        string="Upcoming Timebox",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_upcoming_date_start = fields.Date(
        string="Upcoming Timebox Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_upcoming_date_end = fields.Date(
        string="Upcoming Timebox Date Stop",
        compute="_compute_timebox",
        store=True,
    )
    on_running_timebox = fields.Boolean(
        string="On Running Timebox",
        readonly=True,
        compute="_compute_timebox",
        store=True,
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
    baseline_project_id = fields.Many2one(
        string="Baseline Project",
        comodel_name="project.project",
    )
    baseline_project_starting_timebox_id = fields.Many2one(
        string="Baseline Project Starting Timebox",
        related="baseline_project_id.timebox_starting_id",
    )
    baseline_task_id = fields.Many2one(
        string="Baseline Task",
        comodel_name="project.task",
    )
    baseline_task_upcoming_timebox_id = fields.Many2one(
        string="Baseline Task Upcoming Timebox",
        related="baseline_task_id.timebox_upcoming_id",
    )
    baseline_offset = fields.Integer(
        string="Baseline Offset",
        default=0,
    )
    baseline_target_upcoming_timebox_id = fields.Many2one(
        string="Upcoming Timebox Based On Baseline",
        comodel_name="task.timebox",
        compute="_compute_baseline_target_upcoming_timebox_id",
        store=True,
    )
    upcoming_timebox_diff = fields.Boolean(
        string="Has Difference Upcoming Timebox From Baseline",
        compute="_compute_upcoming_timebox_diff",
        store=True,
    )
    move_forward = fields.Boolean(
        string="Move Forward",
        default=True,
    )
    max_predecessor_latest_timebox = fields.Many2one(
        string="Max Predecessor Latest Timebox",
        comodel_name="task.timebox",
        compute="_compute_max_predecessor_latest_timebox",
        store=True,
    )
    recompute_from_predecessor = fields.Boolean(
        string="Recompute From Predecessor",
        default=True,
    )
    num_of_draft_timebox = fields.Integer(
        string="Num of Draft Timebox",
        compute='_compute_num_timebox',
        store=True
    )
    num_of_done_timebox = fields.Integer(
        string="Num of Done Timebox",
        compute='_compute_num_timebox',
        store=True
    )

    @api.depends(
        "baseline_task_upcoming_timebox_id",
        "baseline_project_starting_timebox_id",
        "baseline_offset",
    )
    def _compute_baseline_target_upcoming_timebox_id(self):
        for record in self:
            record.baseline_target_upcoming_timebox_id = False
            if record.baseline_method == "none":
                continue

            if record.baseline_method == "project":
                result = record.baseline_project_starting_timebox_id
            elif record.baseline_method == "task":
                result = record.baseline_task_upcoming_timebox_id

            if not result:
                continue

            if record.baseline_offset > 0:
                result = result.find_next(record.baseline_offset)
            elif record.baseline_offset < 0:
                result = result.find_previous(abs(record.baseline_offset))
            record.baseline_target_upcoming_timebox_id = result

    @api.depends(
        "baseline_target_upcoming_timebox_id",
        "timebox_upcoming_id",
    )
    def _compute_upcoming_timebox_diff(self):
        for record in self:
            result = True
            if record.baseline_target_upcoming_timebox_id == record.timebox_upcoming_id:
                result = False
            record.upcoming_timebox_diff = result

    @api.depends(
        "predecessor_ids",
        "predecessor_ids.predecessor_task_id.timebox_latest_id",
    )
    def _compute_max_predecessor_latest_timebox(self):
        for record in self:
            result = False
            if self.predecessor_ids:
                latest_timeboxes = self.predecessor_ids.mapped(
                    "target_timebox_from_predecessor"
                ).sorted(key=lambda r: r.date_start)
                if len(latest_timeboxes) > 0:
                    result = latest_timeboxes[-1]
            record.max_predecessor_latest_timebox = result

    @api.onchange(
        "baseline_method",
    )
    def onchange_baseline_project_id(self):
        self.baseline_project_id = False
        if self.baseline_method in ["project", "task"] and self.project_id:
            self.baseline_project_id = self.project_id

    @api.onchange(
        "baseline_project_id",
    )
    def onchange_baseline_task_id(self):
        self.baseline_task_id = False

    def action_move_to_next(self):
        for record in self.sudo():
            record._move_to_next()

    def action_move_to_previous(self):
        for record in self.sudo():
            record._move_to_previous()

    def action_recompute_timebox_from_predecessor(self):
        for record in self.sudo():
            record._recompute_timebox_from_predecessor()

    def action_recompute_sucessor_timebox(self):
        for record in self.sudo():
            record._recompute_sucessor_timebox()

    def action_change_into_target_timebox(self):
        for record in self.sudo():
            record._change_into_target_timebox()

    def _change_into_target_timebox(self):
        self.ensure_one()
        if not self.baseline_target_upcoming_timebox_id:
            return True
        timeboxes = self.timebox_ids.filtered(lambda r: r.state == "done")
        timeboxes += self.baseline_target_upcoming_timebox_id
        self.write({"timebox_ids": [(6, 0, timeboxes.ids)]})

    def _recompute_sucessor_timebox(self):
        self.ensure_one()
        for sucessor in self.sucessor_ids.filtered(
            lambda r: r.task_id.recompute_from_predecessor
        ):
            sucessor.task_id.action_recompute_timebox_from_predecessor()

    def _recompute_timebox_from_predecessor(self):
        self.ensure_one()
        if self.max_predecessor_latest_timebox:
            target_timebox = self.max_predecessor_latest_timebox
            self.write({"timebox_ids": [(4, target_timebox.id)]})

    def _move_to_next(self):
        self.ensure_one()
        current_upcoming_timebox = self.timebox_upcoming_id
        next_timebox = current_upcoming_timebox.find_next()
        if not next_timebox:
            error_message = _(
                """
            Context: Move task to next timebox
            Database ID: %s
            Problem: No timebox
            Solution: Create timebox
            """
                % (self.id)
            )
            raise ValidationError(error_message)
        timeboxes = self.timebox_ids
        timeboxes = timeboxes + next_timebox - current_upcoming_timebox
        self.write({"timebox_ids": [(6, 0, timeboxes.ids)]})

    def _move_to_previous(self):
        self.ensure_one()
        current_upcoming_timebox = self.timebox_upcoming_id
        previous_timebox = current_upcoming_timebox.find_previous()
        if not previous_timebox:
            error_message = _(
                """
            Context: Move task to previous timebox
            Database ID: %s
            Problem: No timebox
            Solution: Create timebox
            """
                % (self.id)
            )
            raise ValidationError(error_message)
        timeboxes = self.timebox_ids
        timeboxes = timeboxes + previous_timebox - current_upcoming_timebox
        self.write({"timebox_ids": [(6, 0, timeboxes.ids)]})
