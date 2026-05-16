# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProjectBatchAssignment(models.Model):
    _name = "project.batch_assignment"
    _inherit = [
        "project.batch_assignment",
        "mixin.documenso_signing_approval",
    ]

    _documenso_signing_create_page = True
