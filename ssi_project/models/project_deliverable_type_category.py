# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProjectDeliverableTypeCategory(models.Model):
    _name = "project_deliverable_type_category"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Project Deliverable Type Category"
