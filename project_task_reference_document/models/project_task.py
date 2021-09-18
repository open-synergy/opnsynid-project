# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    document_reference_ids = fields.One2many(
        string="Document Reference",
        comodel_name="project.task_reference_document",
        inverse_name="task_id",
    )
