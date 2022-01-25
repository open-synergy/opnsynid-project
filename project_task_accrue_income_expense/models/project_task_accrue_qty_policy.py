# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=W0622
from openerp import api, fields, models
from openerp.tools.safe_eval import safe_eval as eval


class ProjectTaskAccrueQtyPolicy(models.Model):
    _name = "project.task_accrue_qty_policy"
    _descrption = "Project Task Accrue Qty Policy"

    name = fields.Char(
        string="Policy",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
    computation_method = fields.Selection(
        string="Computation Method",
        selection=[
            ("code", "Python Code"),
        ],
        required=True,
        default="code",
    )
    python_code = fields.Text(
        string="Python Code",
    )

    def _get_localdict(self, document):
        self.ensure_one()
        return {
            "env": self.env,
            "document": document,
        }

    @api.multi
    def _compute_value(self, document):
        self.ensure_one()
        localdict = self._get_localdict(document)
        try:
            eval(self.python_code, localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except:  # noqa: E722
            result = False
        return result
