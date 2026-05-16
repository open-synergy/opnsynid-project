# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProjectAssignment(models.Model):
    _name = "project.assignment"
    _inherit = [
        "project.assignment",
        "mixin.documenso_signing",
    ]

    _documenso_signing_create_page = True
