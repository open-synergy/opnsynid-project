# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTaskTemplate(models.Model):
    _inherit = "project.task_template"

    instruction_ids = fields.One2many(
        string="Instruction",
        comodel_name="project.task_tmpl_main_instruction",
        inverse_name="task_template_id",
    )
