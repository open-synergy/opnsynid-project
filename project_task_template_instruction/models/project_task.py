# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.depends(
        "task_template_id",
    )
    def _compute_task_template_instruction(self):
        for task in self:
            result = []
            if task.task_template_id and task.task_template_id.instruction_ids:
                for instruction in task.task_template_id.instruction_ids:
                    result.append(instruction.id)
            task.task_tmpl_instruction_ids = [(6, 0, result)]

    task_tmpl_instruction_ids = fields.Many2many(
        string="Instruction Based on Task Template",
        comodel_name="project.task_tmpl_main_instruction",
        compute="_compute_task_template_instruction",
        store=False,
    )
