# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    @api.multi
    @api.depends(
        "project_stage_no_restrict_group_ids",
    )
    def _compute_policy(self):
        _super = super(ProjectProject, self)
        _super._compute_policy()

    no_restrict_ok = fields.Boolean(
        string="Can Move Stages Without Restriction",
        compute="_compute_policy",
        store=False,
    )
    project_stage_no_restrict_group_ids = fields.Many2many(
        string="Allow To Move Stages Without Restriction",
        comodel_name="res.groups",
        relation="rel_project_stage_no_restrict_groups",
        column1="project_id",
        column2="group_id",
    )

    @api.onchange(
        "project_template_id",
    )
    def onchange_project_stage_no_restrict_group_ids(self):
        self.project_stage_no_restrict_group_ids = False
        if self.project_template_id:
            project_template_id = self.project_template_id
            self.project_stage_no_restrict_group_ids =\
                project_template_id.template_stage_no_restrict_group_ids.ids
