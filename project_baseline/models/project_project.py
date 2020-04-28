# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, timedelta
from openerp import api, models, fields, _
from openerp.exceptions import Warning as UserError
from openerp.addons.base.res.res_partner import _tz_get
from pytz import timezone
import logging
_logger = logging.getLogger(__name__)

try:
    import pandas as pd
except (ImportError, IOError) as err:
    _logger.debug(err)


class ProjectProject(models.Model):
    _inherit = "project.project"

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
        "project_timezone",
        "working_time_from",
        "working_time_to",
        "working_day_ids",
    )
    def _compute_baseline_start(self):
        company_uom = self.env.user.company_id.project_time_mode_id
        for project in self:
            if project.project_timezone:
                tz = project.project_timezone
            else:
                tz = self.env.user.tz
            baseline_start = False
            if project.start_schedule_base_on == "manual":
                baseline_start = project.manual_baseline_start
            elif project.start_schedule_base_on == "project_start":
                baseline_start = project.baseline_start_project_id and \
                    project.baseline_start_project_id.baseline_start or \
                    False
            elif project.start_schedule_base_on == "project_finish":
                baseline_start = project.baseline_start_project_id and \
                    project.baseline_start_project_id.baseline_finish or \
                    False
            elif project.start_schedule_base_on == "task_start":
                baseline_start = project.baseline_start_task_id and \
                    project.baseline_start_task_id.baseline_start or \
                    False
            elif project.start_schedule_base_on == "task_finish":
                baseline_start = project.baseline_start_task_id and \
                    project.baseline_start_task_id.baseline_finish or \
                    False

            if baseline_start:
                dt_base_start = datetime.strptime(
                    baseline_start, "%Y-%m-%d %H:%M:%S")
                dt_base_start = timezone("UTC").localize(dt_base_start)
                dt_base_start = dt_base_start.astimezone(timezone(tz))
                dt_base_start = pd.Timestamp(dt_base_start)

                start_offset = 0.0
                start_offset_hours = 0
                start_offset_minutes = 0

                working_time = project._get_working_time()
                working_day = project._get_working_day()
                holiday = project._get_holiday() or None

                cbh = pd.tseries.offsets.CustomBusinessHour(
                    n = start_offset_hours,
                    start = working_time["conv_hour_from"],
                    end = working_time["conv_hour_to"],
                    weekmask = working_day,
                    holidays = holiday,
                )

                dt_start = dt_base_start + cbh + pd.tseries.offsets.Minute(
                    start_offset_minutes)

                dt_start = dt_start.to_pydatetime()
                dt_start = dt_start.astimezone(timezone("UTC"))
                baseline_start = dt_start.strftime("%Y-%m-%d %H:%M:%S")

            project.baseline_start = baseline_start

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
        "project_timezone",
        "working_time_from",
        "working_time_to",
        "working_day_ids",
    )
    def _compute_baseline_finish(self):
        company_uom = self.env.user.company_id.project_time_mode_id
        for project in self:
            if project.project_timezone:
                tz = project.project_timezone
            else:
                tz = self.env.user.tz
            baseline_finish = False
            if project.finish_schedule_base_on == "manual":
                baseline_finish = project.manual_baseline_finish
            elif project.finish_schedule_base_on == "project_start":
                baseline_finish = project.baseline_finish_project_id and \
                    project.baseline_finish_project_id.baseline_start or \
                    False
            elif project.finish_schedule_base_on == "project_finish":
                baseline_finish = project.baseline_finish_project_id and \
                    project.baseline_finish_project_id.baseline_finish or \
                    False
            elif project.finish_schedule_base_on == "task_start":
                baseline_finish = project.baseline_finish_task_id and \
                    project.baseline_finish_task_id.baseline_start or \
                    False
            elif project.finish_schedule_base_on == "task_finish":
                baseline_finish = project.baseline_finish_task_id and \
                    project.baseline_finish_task_id.baseline_finish or \
                    False

            if baseline_finish:

                dt_base_finish = datetime.strptime(
                    baseline_finish, "%Y-%m-%d %H:%M:%S")
                dt_base_finish = timezone("UTC").localize(dt_base_finish)
                dt_base_finish = dt_base_finish.astimezone(timezone(tz))
                dt_base_finish = pd.Timestamp(dt_base_finish)

                finish_offset = 0.0
                finish_offset_hours = 0
                finish_offset_minutes = 0

                if project.finish_offset_uom_id:
                    finish_offset = self.env["product.uom"]._compute_qty_obj(
                        from_unit=project.finish_offset_uom_id,
                        qty=project.finish_offset,
                        to_unit=company_uom,
                    )
                    finish_offset_hours = int(finish_offset)
                    if abs(finish_offset % 1.0) > 0:
                        finish_offset_minutes = abs(
                            int((finish_offset % 1.0) * 60))

                working_time = project._get_working_time()
                working_day = project._get_working_day()
                holiday = project._get_holiday() or None

                cbh = pd.tseries.offsets.CustomBusinessHour(
                    n = finish_offset_hours,
                    start = working_time["conv_hour_from"],
                    end = working_time["conv_hour_to"],
                    weekmask = working_day,
                    holidays = holiday,
                )

                dt_finish = dt_base_finish + cbh + pd.tseries.offsets.Minute(
                    finish_offset_minutes)

                dt_finish = dt_finish.to_pydatetime()
                dt_finish = dt_finish.astimezone(timezone("UTC"))
                baseline_finish = dt_finish.strftime("%Y-%m-%d %H:%M:%S")

            project.baseline_finish = baseline_finish

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
    project_timezone = fields.Selection(
        string="Timezone",
        selection=_tz_get,
    )
    working_time_from = fields.Float(
        string="Work From",
        required=True,
        default=9,
        help="Start and End time of working.",
    )
    working_time_to = fields.Float(
        string="Work To",
        required=True,
        default=17,
    )

    @api.model
    def _default_working_day_ids(self):
        obj_working_day =\
            self.env["project.baseline.working_day"]
        sat = self.env.ref(
            "project_baseline.project_baseline_working_day_sat").id
        sun = self.env.ref(
            "project_baseline.project_baseline_working_day_sun").id
        exception_day = [sat, sun]

        criteria = [
            ("id", "not in", exception_day)
        ]
        return obj_working_day.search(criteria).ids

    working_day_ids = fields.Many2many(
        string="Working Day(s)",
        comodel_name="project.baseline.working_day",
        relation="rel_project_2_working_day",
        column1="project_id",
        column2="working_day_id",
        default=lambda self: self._default_working_day_ids(),
    )

    @api.onchange("baseline_start_project_id")
    def onchage_baseline_start_task_id(self):
        self.baseline_start_task_id = False

    @api.onchange("baseline_finish_project_id")
    def onchage_baseline_finish_task_id(self):
        self.baseline_finish_task_id = False

    @api.multi
    def _get_working_time(self):
        self.ensure_one()
        conv_hour_from =\
            timedelta(hours = self.working_time_from)
        conv_hour_to =\
            timedelta(hours= self.working_time_to)
        return {
            "conv_hour_from": str(conv_hour_from).rsplit(':', 1)[0],
            "conv_hour_to": str(conv_hour_to).rsplit(':', 1)[0],
        }

    @api.multi
    def _get_working_day(self):
        self.ensure_one()
        result = "Mon Tue Wed Thu Fri"
        working_day = self.working_day_ids.mapped("code")

        if working_day:
            result = ' '.join(working_day)
        return result

    def _get_holiday(self):
        """Method for get Public Holiday"""
        result = []
        return result

    @api.constrains(
        "working_time_from",
        "working_time_to"
    )
    def _check_date(self):
        strWarning = _(
            "'Work Form' must be greater than 'Work To'")
        if self.working_time_from and self.working_time_to:
            if self.working_time_from > self.working_time_to:
                raise UserError(strWarning)
