# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class ProjectRole(models.Model):
    _name = "project.role"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Project Role"
