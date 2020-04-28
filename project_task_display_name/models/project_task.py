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
        res = super(ProjectTask, self)\
            .name_search(name=name, args=args, operator=operator, limit=limit)
        args = list(args or [])
        if name:
            criteria = [
                "|",
                ("code", operator, name),
                ("name", operator, name)
            ]
            criteria = criteria + args
            task_ids = self.search(criteria, limit=limit)
            if task_ids:
                return task_ids.name_get()
        return res
