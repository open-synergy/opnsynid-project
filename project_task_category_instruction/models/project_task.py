# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.depends(
        "categ_id",
    )
    def _compute_category_instruction(self):
        for task in self:
            result = []
            if task.categ_id and task.categ_id.instruction_ids:
                for instruction in task.categ_id.instruction_ids:
                    result.append(instruction.id)
            task.categ_instruction_ids = [(6, 0, result)]

    categ_instruction_ids = fields.Many2many(
        string="Instruction Based on Category",
        comodel_name="project.category_main_instruction",
        compute="_compute_category_instruction",
        store=False,
    )
