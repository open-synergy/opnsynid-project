# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    @api.onchange(
        "project_id",
    )
    def onchange_partner_id(self):
        self.partner_id = False
        if self.project_id:
            self.partner_id = self.project_id.partner_id
