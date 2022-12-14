# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class TaskType(models.Model):
    _name = "task.type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Task Type"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="task.type_category",
    )
