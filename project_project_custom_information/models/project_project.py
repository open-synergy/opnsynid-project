# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import api, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = [
        "project.project",
        "custom.info.mixin",
    ]

    @api.onchange(
        "project_template_id",
    )
    def onchange_custom_info_template_id(self):
        self.custom_info_template_id = False
        if self.project_template_id:
            self.custom_info_template_id = (
                self.project_template_id.project_custom_info_template_id
            )
