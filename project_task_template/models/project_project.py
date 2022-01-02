# -*- coding: utf-8 -*-
# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ProjectProject(models.Model):
    _name = "project.project"
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
            ("task_template_id", "=", task_template.id),
        ]
        tasks = obj_task.search(criteria)
        if len(tasks) > 0:
            result = tasks[0]
        return result

    @api.multi
    def create_task_from_template(self):
        for project in self:
            project._create_task_from_template()

    @api.multi
    def _create_task_from_template(self):
        self.ensure_one()
        obj_task = self.env["project.task"]
        self._check_template()
        self._unlink_task_with_template()
        for task_template in self.project_template_id.task_template_ids:
            obj_task.create(task_template._prepare_task_data(self.id))

        for task in self.tasks:
            task.write(task._prepare_post_task_data())

    @api.multi
    def _check_template(self):
        self.ensure_one()
        error_message = _("No project template defined")
        if not self.project_template_id:
            raise UserError(error_message)
        return True

    @api.multi
    def _unlink_task_with_template(self):
        self.ensure_one()
        obj_task = self.env["project.task"]
        criteria = [("project_id", "=", self.id), ("task_template_id", "!=", False)]
        tasks = obj_task.search(criteria)
        tasks.unlink()
