# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectCategoryMainInstruction(models.Model):
    _name = "project.category_main_instruction"
    _descrption = "Project Task Category Instruction"

    categ_id = fields.Many2one(
        string="Task Category",
        comodel_name="project.category.main",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(
        string="Instruction",
        required=True,
    )
    instruction_url = fields.Char(
        string="Instruction URL",
        required=True,
    )
