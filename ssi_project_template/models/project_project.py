# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    template_id = fields.Many2one(
        string="Template",
        comodel_name="project.template",
    )

    def action_create_task_from_template(self):
        for record in self:
            record._create_task_from_template()

    def _create_task_from_template(self):
        self.ensure_one()
        self._unlink_task_created_by_template()
        for task_template in self.template_id.task_template_ids:
            task_template._create_task(self)

    def _unlink_task_created_by_template(self):
        self.ensure_one()
        Task = self.env["project.task"]
        criteria = self._prepare_domain_task_2b_unlink()
        tasks = Task.search(criteria)
        tasks.unlink()

    def _prepare_domain_task_2b_unlink(self):
        self.ensure_one()
        return [
            ("project_id", "=", self.id),
            ("template_id", "!=", False),
        ]
