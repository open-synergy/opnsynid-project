# -*- coding: utf-8 -*-
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, api


class ProjectTask(models.Model):
    _inherit = "project.task"

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
        args = list(args or [])
        if name:
            search_name = name
            if operator != "=":
                search_name = "%s%%" % name
            task_ids = self.search(
                [("code", operator, search_name)] + args,
                limit=limit
            )
            if task_ids.ids:
                return task_ids.name_get()
        return super(ProjectTask, self)\
            .name_search(name=name, args=args, operator=operator, limit=limit)
