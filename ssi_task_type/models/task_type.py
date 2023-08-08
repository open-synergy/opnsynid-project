# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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
    instruction_ids = fields.One2many(
        string="Task Type Instructions",
        comodel_name="task_type.instruction",
        inverse_name="type_id",
    )
    sucessor_ids = fields.One2many(
        string="Task Type Sucessors",
        comodel_name="task_type.sucessor",
        inverse_name="type_id",
    )
