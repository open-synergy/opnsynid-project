# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    is_default = fields.Boolean(string="Is Default?", required=False)
