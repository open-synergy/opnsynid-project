# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTemplateCostAccountMapping(models.Model):
    _name = "project.template_cost_account_mapping"
    _descrption = "Project Template Cost Account Mapping"

    project_template_id = fields.Many2one(
        string="Project Template",
        comodel_name="project.template",
        required=True,
        ondelete="cascade",
    )
    cip_account_id = fields.Many2one(
        string="CIP Account",
        comodel_name="account.account",
        required=True,
        ondelete="restrict",
    )
    cost_account_id = fields.Many2one(
        string="Cost Account",
        comodel_name="account.account",
        required=True,
        ondelete="restrict",
    )
