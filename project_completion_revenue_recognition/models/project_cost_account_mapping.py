# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectCostAccountMapping(models.Model):
    _name = "project.cost_account_mapping"
    _descrption = "Project Cost Account Mapping"

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
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
