# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    def action_create_analytic_account(self):
        for record in self.sudo():
            record._create_analytic_account()

    def _create_analytic_account(self):
        self.ensure_one()
        if self.analytic_account_id:
            return True
        AA = self.env["account.analytic.account"]
        aa = AA.create(self._prepare_create_analytic_account())
        self.write(
            {
                "analytic_account_id": aa.id,
            }
        )

    def _prepare_create_analytic_account(self):
        self.ensure_one()
        group = self.type_id and self.type_id.analytic_group_id
        return {
            "name": self.name,
            "partner_id": self.partner_id.id,
            "group_id": group and group.id or False,
            "currency_id": self.company_id.currency_id.id,
        }
