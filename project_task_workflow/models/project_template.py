# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectTemplate(models.Model):
    _inherit = "project.template"

    template_stage_no_restrict_group_ids = fields.Many2many(
        string="Allow To Move Stages Without Restriction",
        comodel_name="res.groups",
        relation="rel_project_template_stage_no_restrict_groups",
        column1="project_id",
        column2="group_id",
    )
