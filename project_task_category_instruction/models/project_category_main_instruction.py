# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectCategoryMainInstruction(models.Model):
    _name = "project.category_main_instruction"
    _descrption = "Project Task Category Instruction"

    categ_id = fields.Many2one(
        string="Task Category",
        comodel_name="project.category.main",
        required=True,
    )
    name = fields.Char(
        string="Instruction",
        required=True,
    )
    instruction_url = fields.Char(
        string="Instruction URL",
        required=True,
    )
