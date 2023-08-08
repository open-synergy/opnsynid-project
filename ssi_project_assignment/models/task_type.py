# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TaskType(models.Model):
    _name = "task.type"
    _inherit = [
        "task.type",
    ]
    _description = "task.type"

    role_id = fields.Many2one(
        string="Role",
        comodel_name="project.role",
    )
    restrict_assignment = fields.Boolean(
        string="Restrict Assignment",
    )
