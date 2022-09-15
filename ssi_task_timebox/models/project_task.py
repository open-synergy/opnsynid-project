# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


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