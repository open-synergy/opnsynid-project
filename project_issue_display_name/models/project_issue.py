# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    @api.multi
    def name_get(self):
        result = []
        for rec in self:
            if rec.issue_code:
                name = "[{}] {}".format(rec.issue_code, rec.name)
            else:
                name = "%s" % (rec.name)
            result.append((rec.id, name))
        return result

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        res = super(ProjectIssue, self).name_search(
            name=name, args=args, operator=operator, limit=limit
        )
        args = list(args or [])
        if name:
            criteria = ["|", ("issue_code", operator, name), ("name", operator, name)]
            criteria = criteria + args
            project_issue_ids = self.search(criteria, limit=limit)
            if project_issue_ids:
                return project_issue_ids.name_get()
        return res
