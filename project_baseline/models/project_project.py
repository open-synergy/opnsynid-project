# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp import api, models, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    @api.multi
    @api.depends(
        "start_schedule_base_on", "finish_schedule_base_on",
        "baseline_start_task_id", "baseline_start_project_id",
        "baseline_finish_task_id", "baseline_finish_project_id",
        "baseline_start_task_id.baseline_start",
        "baseline_start_task_id.baseline_finish",
        "baseline_finish_task_id.baseline_start",
        "baseline_finish_task_id.baseline_finish",
        "start_offset_uom_id", "start_offset",
        "finish_offset_uom_id", "finish_offset",
    )
    def _compute_baseline(self):
        company_uom = self.env.user.company_id.project_time_mode_id
        for project in self:
            baseline_start = baseline_finish = False
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

            if baseline_start:
                dt_base_start = datetime.strptime(
                    baseline_start, "%Y-%m-%d %H:%M:%S")
                start_offset = 0.0

                if project.start_offset_uom_id:
                    start_offset = self.env["product.uom"]._compute_qty_obj(
                        from_unit=project.start_offset_uom_id,
                        qty=project.start_offset,
                        to_unit=company_uom,
                    )
                dt_start = dt_base_start + relativedelta(hours=+start_offset)
                baseline_start = dt_start.strftime("%Y-%m-%d %H:%M:%S")

            if baseline_finish:

                dt_base_finish = datetime.strptime(
                    baseline_finish, "%Y-%m-%d %H:%M:%S")
                finish_offset = 0.0

                if project.finish_offset_uom_id:
                    finish_offset = self.env["product.uom"]._compute_qty_obj(
                        from_unit=project.finish_offset_uom_id,
                        qty=project.finish_offset,
                        to_unit=company_uom,
                    )
                dt_finish = dt_base_finish + \
                    relativedelta(hours=+finish_offset)
                baseline_finish = dt_finish.strftime("%Y-%m-%d %H:%M:%S")

            project.baseline_start = baseline_start
            project.baseline_finish = baseline_finish

    baseline_start = fields.Datetime(
        string="Baseline Start",
        compute="_compute_baseline",
        store=True,
    )
    baseline_finish = fields.Datetime(
        string="Baseline Finish",
        compute="_compute_baseline",
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
