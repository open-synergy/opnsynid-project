# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    template_id = fields.Many2one(
        string="Template",
        comodel_name="task.template",
    )

    @api.onchange(
        "template_id",
    )
    def onchange_type_id(self):
        self.type_id = False

        if self.template_id and self.template_id.type_id:
            self.type_id = self.template_id.type_id
