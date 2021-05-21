# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    duplicate_issue_id = fields.Many2one(
        string="Duplicate Issue",
        comodel_name="project.issue",
    )
    duplicate_issue_ids = fields.One2many(
        string="List Duplicate Issue",
        comodel_name="project.issue",
        inverse_name="duplicate_issue_id",
        readonly=True,
    )
