# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectCategoryMain(models.Model):
    _name = "project.category.main"
    _inherit = "project.category.main"

    category_custom_info_template_id = fields.Many2one(
        string="Custom Info Template",
        comodel_name="custom.info.template",
    )
