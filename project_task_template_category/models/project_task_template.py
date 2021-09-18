# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectTaskTemplate(models.Model):
    _inherit = "project.task_template"

    categ_id = fields.Many2one(
        string="Category",
        comodel_name="project.category.main",
    )

    @api.multi
    def _prepare_task_data(self, project_id):
        _super = super(ProjectTaskTemplate, self)
        result = _super._prepare_task_data(project_id)
        result.update({"categ_id": self.categ_id and self.categ_id.id or False})
        return result
