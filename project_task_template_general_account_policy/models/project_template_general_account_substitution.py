# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTemplateGeneralAccountSubstitution(models.Model):
    _name = "project.template_general_account_substitution"
    _description = "General Account Substitution"

    project_template_id = fields.Many2one(
        string="Project Template",
        comodel_name="projct.template",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    expense_general_account_id = fields.Many2one(
        string="Expense General Account",
        comodel_name="account.account",
    )
    income_general_account_id = fields.Many2one(
        string="Income General Account",
        comodel_name="account.account",
    )
