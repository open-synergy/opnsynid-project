# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="task.type",
    )
    type_category_id = fields.Many2one(
        string="Type Category",
        comodel_name="task.type_category",
        related="type_id.category_id",
        store=True,
    )
