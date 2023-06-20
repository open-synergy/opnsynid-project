# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    template_id = fields.Many2one(
        string="Template",
        comodel_name="project.template",
    )

    @api.onchange(
        "template_id",
    )
    def onchange_type_id(self):
        self.type_id = False

        if self.template_id and self.template_id.type_id:
            self.type_id = self.template_id.type_id

    def action_create_task_from_template(self):
        for record in self:
            record._create_task_from_template()

    def _get_parent_task_template_ids(self):
        self.ensure_one()
        task_template_ids = []
        current_task_template = self.template_id
        while current_task_template:
            task_template_ids.insert(0, current_task_template.task_template_ids)
            if not current_task_template.parent_id:
                return task_template_ids
            current_task_template = current_task_template.parent_id

    def _create_task_from_template(self):
        self.ensure_one()
        self._unlink_task_created_by_template()
        task_template_ids = self._get_parent_task_template_ids()
        for task_template in task_template_ids:
            for template in task_template:
                template._create_task(self)

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
