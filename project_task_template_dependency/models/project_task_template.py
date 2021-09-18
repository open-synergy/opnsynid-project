# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTaskTemplate(models.Model):
    _inherit = "project.task_template"

    predecessor_ids = fields.One2many(
        string="Predecessor",
        comodel_name="project.task_template_dependency",
        inverse_name="task_id",
    )
    sucessor_ids = fields.One2many(
        string="Sucessor",
        comodel_name="project.task_template_dependency",
        inverse_name="predecessor_task_id",
    )
