# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TaskTypeInstruction(models.Model):
    _name = "task_type.instruction"
    _description = "Task Type Instruction"
    _order = "sequence, id"

    type_id = fields.Many2one(
        string="Task Type",
        comodel_name="task.type",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
        required=True,
    )
    name = fields.Char(
        string="Instruction Name",
        required=True,
    )
    url = fields.Char(
        string="Instruction URL",
        required=True,
    )
