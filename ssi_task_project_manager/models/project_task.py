# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    project_manager_id = fields.Many2one(
        string="Project Manager",
        comodel_name="res.users",
        related="project_id.user_id",
        store=True,
    )
