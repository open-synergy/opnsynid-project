# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    @api.depends(
        "task_ids",
        "task_ids.timebox_latest_id",
        "task_ids.timebox_date_start",
        "task_ids.timebox_date_stop",
        "task_ids.timebox_initial_id",
        "task_ids.timebox_initial_date_start",
        "task_ids.timebox_initial_date_stop",
        "task_ids.timebox_upcoming_id",
        "task_ids.timebox_upcoming_date_start",
        "task_ids.timebox_upcoming_date_stop",
    )
    @api.multi
    def _compute_timebox(self):
        for document in self:
            timebox_latest_id = (
                timebox_latest_date_start
            ) = (
                timebox_latest_date_stop
            ) = (
                timebox_initial_id
            ) = timebox_initial_date_start = timebox_initial_date_stop = False

            if document.task_ids:
                tasks = document.task_ids
                latest_sorted = tasks.sorted(key=lambda r: r.timebox_latest_id)
                timebox_latest_id = latest_sorted[-1].timebox_latest_id
                timebox_latest_date_start = timebox_latest_id.date_start
                timebox_latest_date_stop = timebox_latest_id.date_stop
                initial_sorted = tasks.sorted(key=lambda r: r.timebox_initial_id)
                timebox_initial_id = initial_sorted[0].timebox_initial_id
                timebox_initial_date_start = timebox_initial_id.date_start
                timebox_initial_date_stop = timebox_initial_id.date_stop

            document.timebox_latest_id = timebox_latest_id
            document.timebox_latest_date_start = timebox_latest_date_start
            document.timebox_latest_date_stop = timebox_latest_date_stop
            document.timebox_initial_id = timebox_initial_id
            document.timebox_initial_date_start = timebox_initial_date_start
            document.timebox_initial_date_stop = timebox_initial_date_stop

    timebox_latest_id = fields.Many2one(
        string="Letest Timebox",
        comodel_name="project.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_latest_date_start = fields.Date(
        string="Latest Timebox Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_latest_date_stop = fields.Date(
        string="Lates Timebox Date Stop",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_id = fields.Many2one(
        string="Timebox Initial",
        comodel_name="project.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_start = fields.Date(
        string="Timebox Initial Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_stop = fields.Date(
        string="Timebox Initial Date Stop",
        compute="_compute_timebox",
        store=True,
    )
