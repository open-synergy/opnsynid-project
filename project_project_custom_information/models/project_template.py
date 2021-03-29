# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectTemplate(models.Model):
    _inherit = "project.template"

    project_custom_info_template_id = fields.Many2one(
        string="Custom Info Template",
        comodel_name="custom.info.template",
    )
