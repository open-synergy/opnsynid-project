# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectRevenueAccountMapping(models.Model):
    _name = "project.revenue_account_mapping"
    _descrption = "Project Revenue Account Mapping"

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        required=True,
        ondelete="cascade",
    )
    billing_cip_account_id = fields.Many2one(
        string="Billing on CIP Account",
        comodel_name="account.account",
        required=True,
        ondelete="restrict",
    )
    revenue_account_id = fields.Many2one(
        string="Revenue Account",
        comodel_name="account.account",
        required=True,
        ondelete="restrict",
    )
