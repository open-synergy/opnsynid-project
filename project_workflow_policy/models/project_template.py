# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectTemplate(models.Model):
    _inherit = "project.template"

    project_reopen_grp_ids = fields.Many2many(
        string="Allowed to Re-Open Project",
        comodel_name="res.groups",
        relation="rel_project_template_2_reopen_groups",
        column1="project_template_id",
        column2="group_id",
    )

    project_close_grp_ids = fields.Many2many(
        string="Allowed to Close Project",
        comodel_name="res.groups",
        relation="rel_project_template_2_close_groups",
        column1="project_template_id",
        column2="group_id",
    )

    project_pending_grp_ids = fields.Many2many(
        string="Allowed to Pending",
        comodel_name="res.groups",
        relation="rel_project_template_2_pending_groups",
        column1="project_template_id",
        column2="group_id",
    )

    project_set_template_grp_ids = fields.Many2many(
        string="Allowed to Set as Template",
        comodel_name="res.groups",
        relation="rel_project_template_2_set_template_groups",
        column1="project_template_id",
        column2="group_id",
    )

    project_new_grp_ids = fields.Many2many(
        string="Allowed to New Project Based on Template",
        comodel_name="res.groups",
        relation="rel_project_template_2_new_groups",
        column1="project_template_id",
        column2="group_id",
    )

    project_reset_grp_ids = fields.Many2many(
        string="Allowed to Reset as Project",
        comodel_name="res.groups",
        relation="rel_project_template_2_reset_groups",
        column1="project_template_id",
        column2="group_id",
    )

    project_cancel_grp_ids = fields.Many2many(
        string="Allowed to Cancel Project",
        comodel_name="res.groups",
        relation="rel_project_template_2_cancel_groups",
        column1="project_template_id",
        column2="group_id",
    )
