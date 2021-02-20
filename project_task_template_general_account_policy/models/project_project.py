# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    @api.onchange(
        "project_template_id",
    )
    def onchange_general_account_substitution_ids(self):
        self.update({"general_account_substitution_ids": [(5, 0, 0)]})
        if self.project_template_id:
            result = []
            template = self.project_template_id
            for line in template.general_account_substitution_ids:
                exp_account = line.expense_general_account_id
                inc_account = line.income_general_account_id
                result.append(
                    (
                        0,
                        0,
                        {
                            "product_id": line.product_id.id,
                            "expense_general_account_id": exp_account
                            and exp_account.id
                            or False,
                            "income_general_account_id": inc_account
                            and inc_account.id
                            or False,
                        },
                    )
                )
            self.update({"general_account_substitution_ids": result})
