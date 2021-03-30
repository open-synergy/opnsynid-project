# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectCategoryMainInstruction(models.Model):
    _name = "project.task_tmpl_main_instruction"
    _descrption = "Project Task Template Instruction"

    task_template_id = fields.Many2one(
        string="Task Template",
        comodel_name="project.task_template",
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
