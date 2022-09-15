# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = [
        "project.project",
        "mixin.work_object",
    ]

    _work_log_create_page = True

    analytic_account_ids = fields.Many2many(
        string="Allowed Analytic Account(s)",
        comodel_name="account.analytic.account",
        relation="rel_project_2_analytic_account",
        column1="project_id",
        column2="analytic_account_id",
    )
