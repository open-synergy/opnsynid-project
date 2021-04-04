# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = [
        "project.task",
        "custom.info.mixin",
    ]

    @api.onchange(
        "categ_id",
    )
    def onchange_custom_info_template_id(self):
        self.custom_info_template_id = False
        if self.categ_id:
            categ = self.categ_id
            custom_template = categ.category_custom_info_template_id
            self.custom_info_template_id = custom_template
