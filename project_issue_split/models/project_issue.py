# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    split_issue_id = fields.Many2one(
        string="Split Issue From",
        comodel_name="project.issue",
    )
    split_issue_ids = fields.One2many(
        string="Split Issue Into",
        comodel_name="project.issue",
        inverse_name="split_issue_id",
        readonly=True,
    )