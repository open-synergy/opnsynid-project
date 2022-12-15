# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class TaskType(models.Model):
    _name = "task.type"
    _inherit = [
        "task.type",
    ]

    work_estimation = fields.Float(
        string="Work Estimation",
    )
