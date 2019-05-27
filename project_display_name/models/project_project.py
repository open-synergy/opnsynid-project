# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    @api.multi
    def name_get(self):
        result = []
        for rec in self:
            if rec.code:
                name = "[%s] %s" % (rec.code, rec.name)
            else:
                name = "%s" % (rec.name)
            result.append((rec.id, name))
        return result
