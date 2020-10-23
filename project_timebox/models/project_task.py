# -*- coding: utf-8 -*-
# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    @api.depends(
        "timebox_ids",
        "timebox_ids.date_start",
        "timebox_ids.date_stop",
    )
    @api.multi
    def _compute_timebox(self):
        for document in self:
            timebox_latest_id = timebox_date_start = timebox_date_stop = False
            if len(document.timebox_ids) > 0:
                timebox_latest_id = document.timebox_ids[-1]
                timebox_date_start = timebox_latest_id.date_start
                timebox_date_stop = timebox_latest_id.date_stop
            document.timebox_latest_id = timebox_latest_id
            document.timebox_date_start = timebox_date_start
            document.timebox_date_stop = timebox_date_stop

    timebox_ids = fields.Many2many(
        string="Timeboxes",
        comodel_name="project.timebox",
        relation="rel_timebox_2_task",
        column1="task_id",
        column2="timebox_id",
    )
    timebox_latest_id = fields.Many2one(
        string="Timebox",
        comodel_name="project.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_date_start = fields.Date(
        stting="Timebox Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_date_stop = fields.Date(
        stting="Timebox Date Stop",
        compute="_compute_timebox",
        store=True,
    )

    @api.depends(
        "timebox_ids",
        "timebox_ids.date_start",
        "timebox_ids.date_stop",
    )
    @api.multi
    def _compute_timebox_initial(self):
        for document in self:
            timebox_initial_id = False
            timebox_initial_date_start = False
            timebox_initial_date_stop = False
            if len(document.timebox_ids) > 0:
                timebox_initial_id = document.timebox_ids[0]
                timebox_initial_date_start = timebox_initial_id.date_start
                timebox_initial_date_stop = timebox_initial_id.date_stop
            document.timebox_initial_id = timebox_initial_id
            document.timebox_initial_date_start = timebox_initial_date_start
            document.timebox_initial_date_stop = timebox_initial_date_stop

    timebox_initial_id = fields.Many2one(
        string="Timebox Initial ID",
        comodel_name="project.timebox",
        compute="_compute_timebox_initial",
        store=True,
    )
    timebox_initial_date_start = fields.Date(
        stting="Timebox Initial Date Start",
        compute="_compute_timebox_initial",
        store=True,
    )
    timebox_initial_date_stop = fields.Date(
        stting="Timebox Initial Date Stop",
        compute="_compute_timebox_initial",
        store=True,
    )
