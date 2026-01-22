# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectBatchAssignment(models.Model):
    _name = "project.batch_assignment"
    _inherit = [
        "project.batch_assignment",
        "mixin.single_operating_unit",
    ]

    operating_unit_id = fields.Many2one(
        related="project_id.operating_unit_id",
        store=True,
        compute_sudo=True,
        default=False,
    )
