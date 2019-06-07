# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectTaskTemplate(models.Model):
    _inherit = "project.task_template"

    start_schedule_base_on = fields.Selection(
        string="Start Schedule Based On",
        selection=[
            ("manual", "Manual"),
            ("task_start", "Task Baseline Start"),
            ("task_finish", "Task Baseline Finish"),
        ],
        required=True,
        default="manual",
    )
    baseline_start_task_id = fields.Many2one(
        string="Task Based Schedule",
        comodel_name="project.task_template",
    )
    finish_schedule_base_on = fields.Selection(
        string="Finish Schedule Based On",
        selection=[
            ("manual", "Manual"),
            ("task_start", "Task Baseline Start"),
            ("task_finish", "Task Baseline Finish"),
        ],
        required=True,
        default="manual",
    )
    baseline_finish_task_id = fields.Many2one(
        string="Task Based Schedule",
        comodel_name="project.task_template",
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
