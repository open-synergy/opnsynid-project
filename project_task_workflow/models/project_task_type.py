# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    allowed_stage_ids = fields.Many2many(
        string="Allowed Stages",
        comodel_name="project.task.type",
        relation="rel_stage_allowed_stage",
        column1="parent_stage_id",
        column2="stage_id",
    )
