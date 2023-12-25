# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    timebox_starting_id = fields.Many2one(
        string="Starting Timebox",
        comodel_name="task.timebox",
    )
