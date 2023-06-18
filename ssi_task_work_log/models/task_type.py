# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class TaskType(models.Model):
    _name = "task.type"
    _inherit = [
        "task.type",
    ]

    work_estimation = fields.Float(
        string="Work Estimation",
    )
    work_estimation_offset_0 = fields.Float(
        string="Work Estimation Offset for Low Difficulty",
    )
    work_estimation_offset_1 = fields.Float(
        string="Work Estimation Offset for Medium Difficulty",
    )
    work_estimation_offset_2 = fields.Float(
        string="Work Estimation Offset for High Difficulty",
    )
    work_estimation_offset_3 = fields.Float(
        string="Work Estimation Offset for Very High Difficulty",
    )
    match_aa_partner = fields.Boolean(
        string="Match AA Partner",
    )
    num_of_max_aa = fields.Integer(
        string="Max Num. of AA",
        default=0,
    )
    work_log_analytic_account_ids = fields.Many2many(
        string="Work Log Analytic Account",
        comodel_name="account.analytic.account",
        relation="rel_task_type_2_work_log_aa",
        column1="type_id",
        column2="analytic_account_id",
    )
    work_log_analytic_group_ids = fields.Many2many(
        string="Work Log Analytic Group",
        comodel_name="account.analytic.group",
        relation="rel_task_type_2_work_log_ag",
        column1="type_id",
        column2="analytic_group_id",
    )
    work_log_product_ids = fields.Many2many(
        string="Work Log Products",
        comodel_name="product.product",
        relation="rel_task_type_2_work_log_product",
        column1="type_id",
        column2="product_id",
    )
