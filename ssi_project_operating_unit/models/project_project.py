# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = [
        "project.project",
        "mixin.single_operating_unit",
    ]
