# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = [
        "project.task",
        "mixin.data_requirement",
    ]
    _data_requirement_create_page = True
    _data_requirement_partner_field_name = "partner_id"

    data_requirement_ids = fields.Many2many(
        relation="rel_task_2_data_requirement",
        column1="task_id",
        column2="data_requirement_id",
    )
