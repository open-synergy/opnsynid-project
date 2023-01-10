# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = [
        "project.task",
        "mixin.work_object",
    ]
    _work_log_create_page = True

    work_log_analytic_account_ids = fields.Many2many(
        string="Work Log Analytic Account",
        comodel_name="account.analytic.account",
        relation="rel_task_2_work_log_aa",
        column1="task_id",
        column2="analytic_account_id",
    )

    @api.onchange(
        "type_id",
    )
    def onchange_work_estimation(self):
        self.work_estimation = 0.0
        if self.type_id:
            self.work_estimation = self.type_id.work_estimation
