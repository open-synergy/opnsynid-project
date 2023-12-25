# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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

    def _compute_task_timebox_baseline_from_template(self):
        self.ensure_one()
        template = self.template_id
        data = {}

        if template.baseline_method == "none":
            data.update(
                {
                    "baseline_method": "none",
                }
            )
        elif template.baseline_method == "project":
            data.update(
                {
                    "baseline_method": "project",
                    "baseline_project_id": self.project_id.id,
                    "baseline_offset": template.baseline_offset,
                }
            )
        else:
            criteria = [
                ("project_id", "=", self.project_id.id),
                ("template_id", "=", template.baseline_task_template_id.id),
            ]
            Task = self.env["project.task"]
            tasks = Task.search(criteria)
            data.update(
                {
                    "baseline_method": "task",
                    "baseline_project_id": self.project_id.id,
                    "baseline_offset": template.baseline_offset,
                }
            )
            if len(tasks) > 0:
                data.update(
                    {
                        "baseline_task_id": tasks[0].id,
                    }
                )
        self.write(data)
