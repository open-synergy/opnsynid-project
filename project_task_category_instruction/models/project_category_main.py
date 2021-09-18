# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectCategoryMain(models.Model):
    _inherit = "project.category.main"

    instruction_ids = fields.One2many(
        string="Instruction",
        comodel_name="project.category_main_instruction",
        inverse_name="categ_id",
    )
