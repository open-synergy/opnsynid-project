# -*- coding: utf-8 -*-
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import api, fields, models


class ProjectTaskTemplate(models.Model):
    _inherit = "project.task_template"

    review_planned_hours = fields.Float(string="Review Planned Hours")

    @api.multi
    def _prepare_task_data(self, project_id):
        _super = super(ProjectTaskTemplate, self)
        result = _super._prepare_task_data(project_id)
        result.update({"review_planned_hours": self.review_planned_hours})
        return result
