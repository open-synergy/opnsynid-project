# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectDeliverableType(models.Model):
    _name = "project_deliverable_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Project Deliverable Type"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="project_deliverable_type_category",
        required=True,
    )
