# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTemplate(models.Model):
    _name = "project.template"
    _inherit = "project.template"

    general_account_substitution_ids = fields.One2many(
        string="General Account Substitutions",
        comodel_name="project.template_general_account_substitution",
        inverse_name="project_template_id",
    )
