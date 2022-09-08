# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="project.type",
    )
