# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = [
        "project.project",
        "base.workflow_policy_object",
    ]

    @api.multi
    @api.depends(
        "project_template_id",
    )
    def _compute_policy(self):
        _super = super(ProjectProject, self)
        _super._compute_policy()

    reopen_ok = fields.Boolean(
        string="Can Re-Open Project",
        compute="_compute_policy",
        store=False,
    )
    close_ok = fields.Boolean(
        string="Can Close Project",
        compute="_compute_policy",
        store=False,
    )
    pending_ok = fields.Boolean(
        string="Can Pending",
        compute="_compute_policy",
        store=False,
    )
    set_template_ok = fields.Boolean(
        string="Can Set as Template",
        compute="_compute_policy",
        store=False,
    )
    new_ok = fields.Boolean(
        string="Can New Project Based on Template",
        compute="_compute_policy",
        store=False,
    )
    reset_ok = fields.Boolean(
        string="Can Reset as Project",
        compute="_compute_policy",
        store=False,
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
        store=False,
    )
