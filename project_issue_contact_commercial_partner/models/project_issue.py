# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    commercial_partner_id = fields.Many2one(
        string="Contact's Commercial Partner",
        comodel_name="res.partner",
        related="partner_id.commercial_partner_id",
        store=True,
        readonly=True,
    )
