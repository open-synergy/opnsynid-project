# -*- coding: utf-8 -*-
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = [
        "project.project",
        "mixin.related_attachment",
    ]
