# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TaskTypeSucessor(models.Model):
    _name = "task_type.sucessor"
    _description = "Task Type Sucessor"
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
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
    )
    sucessor_type_id = fields.Many2one(
        string="Sucessor Task Type",
        comodel_name="task.type",
        required=True,
    )
    user_id = fields.Many2one(
        string="Assigned To",
        comodel_name="res.users",
    )
