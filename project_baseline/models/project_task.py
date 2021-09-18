# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from openerp import api, fields, models
from pytz import timezone

_logger = logging.getLogger(__name__)

try:
    import pandas as pd
except (ImportError, IOError) as err:
    _logger.debug(err)


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    @api.depends(
        "start_schedule_base_on",
        "baseline_start_task_id",
        "baseline_start_project_id",
        "baseline_start_task_id.baseline_start",
        "baseline_start_task_id.baseline_finish",
        "baseline_start_project_id.baseline_start",
        "baseline_start_project_id.baseline_finish",
        "start_offset_uom_id",
        "start_offset",
        "manual_baseline_start",
        "project_id",
        "project_id.project_timezone",
        "project_id.resource_calendar_id",
    )
    def _compute_baseline_start(self):
        company_uom = self.env.user.company_id.project_time_mode_id
        for task in self:
            baseline_start = False
            if task.project_id and task.project_id.project_timezone:
                tz = task.project_id.project_timezone
            else:
                tz = self.env.user.tz
            if task.start_schedule_base_on == "manual":
                baseline_start = task.manual_baseline_start
            elif task.start_schedule_base_on == "project_start":
                baseline_start = (
                    task.baseline_start_project_id
                    and task.baseline_start_project_id.baseline_start
                    or False
                )
            elif task.start_schedule_base_on == "project_finish":
                baseline_start = (
                    task.baseline_start_project_id
                    and task.baseline_start_project_id.baseline_finish
                    or False
                )
            elif task.start_schedule_base_on == "task_start":
                baseline_start = (
                    task.baseline_start_task_id
                    and task.baseline_start_task_id.baseline_start
                    or False
                )
            elif task.start_schedule_base_on == "task_finish":
                baseline_start = (
                    task.baseline_start_task_id
                    and task.baseline_start_task_id.baseline_finish
                    or False
                )

            if baseline_start:
                dt_base_start = datetime.strptime(baseline_start, "%Y-%m-%d %H:%M:%S")
                dt_base_start = timezone("UTC").localize(dt_base_start)
                dt_base_start = dt_base_start.astimezone(timezone(tz))
                dt_base_start = pd.Timestamp(dt_base_start)

                start_offset = 0.0
                start_offset_hours = 0
                start_offset_minutes = 0

                if task.start_offset_uom_id:
                    start_offset = self.env["product.uom"]._compute_qty_obj(
                        from_unit=task.start_offset_uom_id,
                        qty=task.start_offset,
                        to_unit=company_uom,
                    )
                    start_offset_hours = int(start_offset)
                    if abs(start_offset % 1.0) > 0:
                        start_offset_minutes = abs(int((start_offset % 1.0) * 60))

                dt_start = (
                    dt_base_start
                    + pd.tseries.offsets.BusinessHour(start_offset_hours)
                    + pd.tseries.offsets.Minute(start_offset_minutes)
                )
                dt_start = dt_start.to_pydatetime()
                dt_start = dt_start.astimezone(timezone("UTC"))
                baseline_start = dt_start.strftime("%Y-%m-%d %H:%M:%S")

            task.baseline_start = baseline_start

    @api.multi
    @api.depends(
        "finish_schedule_base_on",
        "baseline_finish_task_id",
        "baseline_finish_project_id",
        "baseline_finish_task_id.baseline_start",
        "baseline_finish_task_id.baseline_finish",
        "baseline_finish_project_id.baseline_start",
        "baseline_finish_project_id.baseline_finish",
        "finish_offset_uom_id",
        "finish_offset",
        "manual_baseline_finish",
        "project_id",
        "project_id.project_timezone",
        "project_id.resource_calendar_id",
    )
    def _compute_baseline_finish(self):
        company_uom = self.env.user.company_id.project_time_mode_id
        for task in self:
            baseline_finish = False
            if task.project_id and task.project_id.project_timezone:
                tz = task.project_id.project_timezone
            else:
                tz = self.env.user.tz
            if task.finish_schedule_base_on == "manual":
                baseline_finish = task.manual_baseline_finish
            elif task.finish_schedule_base_on == "project_start":
                baseline_finish = (
                    task.baseline_finish_project_id
                    and task.baseline_finish_project_id.baseline_start
                    or False
                )
            elif task.finish_schedule_base_on == "project_finish":
                baseline_finish = (
                    task.baseline_finish_project_id
                    and task.baseline_finish_project_id.baseline_finish
                    or False
                )
            elif task.finish_schedule_base_on == "task_start":
                baseline_finish = (
                    task.baseline_finish_task_id
                    and task.baseline_finish_task_id.baseline_start
                    or False
                )
            elif task.finish_schedule_base_on == "task_finish":
                baseline_finish = (
                    task.baseline_finish_task_id
                    and task.baseline_finish_task_id.baseline_finish
                    or False
                )

            if baseline_finish:

                dt_base_finish = datetime.strptime(baseline_finish, "%Y-%m-%d %H:%M:%S")
                dt_base_finish = timezone("UTC").localize(dt_base_finish)
                dt_base_finish = dt_base_finish.astimezone(timezone(tz))
                dt_base_finish = pd.Timestamp(dt_base_finish)

                finish_offset = 0.0
                finish_offset_hours = 0
                finish_offset_minutes = 0

                if task.finish_offset_uom_id:
                    finish_offset = self.env["product.uom"]._compute_qty_obj(
                        from_unit=task.finish_offset_uom_id,
                        qty=task.finish_offset,
                        to_unit=company_uom,
                    )
                    finish_offset_hours = int(finish_offset)
                    if abs(finish_offset % 1.0) > 0:
                        finish_offset_minutes = abs(int((finish_offset % 1.0) * 60))

                dt_finish = (
                    dt_base_finish
                    + pd.tseries.offsets.BusinessHour(finish_offset_hours)
                    + pd.tseries.offsets.Minute(finish_offset_minutes)
                )
                dt_finish = dt_finish.to_pydatetime()
                dt_finish = dt_finish.astimezone(timezone("UTC"))
                baseline_finish = dt_finish.strftime("%Y-%m-%d %H:%M:%S")

            task.baseline_finish = baseline_finish

    baseline_start = fields.Datetime(
        string="Baseline Start",
        compute="_compute_baseline_start",
        store=True,
    )
    baseline_finish = fields.Datetime(
        string="Baseline Finish",
        compute="_compute_baseline_finish",
        store=True,
    )
    start_schedule_base_on = fields.Selection(
        string="Start Schedule Based On",
        selection=[
            ("manual", "Manual"),
            ("task_start", "Task Baseline Start"),
            ("task_finish", "Task Baseline Finish"),
            ("project_start", "Project Baseline Start"),
            ("project_finish", "Project Baseline Finish"),
        ],
        required=True,
        default="manual",
    )
    baseline_start_task_id = fields.Many2one(
        string="Task Based Schedule",
        comodel_name="project.task",
        store=True,
    )
    baseline_start_project_id = fields.Many2one(
        string="Project Based Schedule",
        comodel_name="project.project",
    )
    finish_schedule_base_on = fields.Selection(
        string="Finish Schedule Based On",
        selection=[
            ("manual", "Manual"),
            ("task_start", "Task Baseline Start"),
            ("task_finish", "Task Baseline Finish"),
            ("project_start", "Project Baseline Start"),
            ("project_finish", "Project Baseline Finish"),
        ],
        required=True,
        default="manual",
    )
    baseline_finish_task_id = fields.Many2one(
        string="Task Based Schedule",
        comodel_name="project.task",
        store=True,
    )
    baseline_finish_project_id = fields.Many2one(
        string="Project Based Schedule",
        comodel_name="project.project",
    )
    manual_baseline_start = fields.Datetime(
        string="Manual Baseline Start",
    )
    manual_baseline_finish = fields.Datetime(
        string="Manual Baseline Finish",
    )
    start_offset = fields.Float(
        string="Baseline Start Offset",
    )
    start_offset_uom_id = fields.Many2one(
        string="Start Offset UoM",
        comodel_name="product.uom",
    )
    finish_offset = fields.Float(
        string="Baseline Finish Offset",
    )
    finish_offset_uom_id = fields.Many2one(
        string="Finish Offset UoM",
        comodel_name="product.uom",
    )

    @api.onchange("baseline_start_project_id")
    def onchage_baseline_start_task_id(self):
        self.baseline_start_task_id = False

    @api.onchange("baseline_finish_project_id")
    def onchage_baseline_finish_task_id(self):
        self.baseline_finish_task_id = False
