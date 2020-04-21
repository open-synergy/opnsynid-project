# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
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

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        res = super(ProjectProject, self)\
            .name_search(name=name, args=args, operator=operator, limit=limit)
        args = list(args or [])
        if name:
            project_ids = self.search(
                ["|", ("code", operator, name), ("name", operator, name)] + args,
                limit=limit
            )
            if project_ids:
                return project_ids.name_get()
        return res
