# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectAssignment(models.Model):
    _name = "project.assignment"
    _inherit = "project.assignment"

    batch_id = fields.Many2one(
        string="# Batch",
        comodel_name="project.batch_assignment",
        readonly=True,
    )
