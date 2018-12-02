# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    project_template_id = fields.Many2one(
        string="Template",
        comodel_name="project.template",
    )

    @api.multi
    def _get_task_from_template(self, task_template):
        self.ensure_one()
        obj_task = self.env["project.task"]
        criteria = [
            ("project_id", "=", self.id),
            ("task_template_id", "=", task_template.id)
        ]
        tasks = obj_task.search(criteria)
        if len(tasks) > 0:
            result = tasks[0]
        return result
