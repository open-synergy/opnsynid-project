# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    task_sequence_id = fields.Many2one(
        string="Task Sequence",
        comodel_name="ir.sequence",
    )
