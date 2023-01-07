# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class TaskInstruction(models.Model):
    _name = "task.instruction"
    _descrption = "Task Instruction"
    _order = "sequence, id"

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
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
