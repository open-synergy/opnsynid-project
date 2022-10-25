# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectType(models.Model):
    _name = "project.type"
    _inherit = [
        "project.type",
    ]

    analytic_group_id = fields.Many2one(
        string="Analytic Group",
        comodel_name="account.analytic.group",
    )
