# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTemplate(models.Model):
    _name = "project.template"
    _inherit = "project.template"

    allowed_cip_account_ids = fields.Many2many(
        string="Allowed CIP Accounts",
        comodel_name="account.account",
        relation="rel_project_template_2_cip_account",
        column1="project_template_id",
        column2="account_id",
    )
    allowed_billing_cip_account_ids = fields.Many2many(
        string="Allowed Billing CIP Accounts",
        comodel_name="account.account",
        relation="rel_project_template_2_billing_cip_account",
        column1="project_template_id",
        column2="account_id",
    )
    cost_account_mapping_ids = fields.One2many(
        string="Cost Account Mapping",
        comodel_name="project.template_cost_account_mapping",
        inverse_name="project_template_id",
    )
    revenue_account_mapping_ids = fields.One2many(
        string="Revenue Account Mapping",
        comodel_name="project.template_revenue_account_mapping",
        inverse_name="project_template_id",
    )
    revenue_recognition_on_project_completion = fields.Boolean(
        string="Recognize Project When Project Close",
        default=False,
    )
    project_completion_journal_id = fields.Many2one(
        string="Project Completion Journal",
        comodel_name="account.journal",
    )
