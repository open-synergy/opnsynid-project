# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class ProjectBatchAssignment(models.Model):
    _name = "project.batch_assignment"
    _inherit = [
        "project.batch_assignment",
        "mixin.qc_worksheet",
    ]
    _qc_worksheet_create_page = True
