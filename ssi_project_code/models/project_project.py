# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import _, api, fields, models
from odoo.osv import expression


class ProjectProject(models.Model):
    _inherit = "project.project"

    code = fields.Char(
        string="Reference",
    )

    _sql_constraints = [
        ("project_project_unique_code", "UNIQUE (code)", _("The code must be unique!")),
    ]

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        default["code"] = ""
        return super().copy(default)

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        if operator in ("ilike", "like", "=", "=like", "=ilike"):
            args = expression.AND(
                [args or [], ["|", ("code", operator, name), ("name", operator, name)]]
            )
            return self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return super(ProjectProject, self)._name_search(
            name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid
        )

    def name_get(self):
        res = []
        for document in self:
            name = document.name
            if document.code:
                name = "[" + document.code + "] " + name
            res.append((document.id, name))
        return res
