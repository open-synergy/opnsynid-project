# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    def _get_baseline_start_task(self):
        self.ensure_one()
        template = self.task_template_id
        if template.start_schedule_base_on not in ["task_start", "task_finish"]:
            return False

        task_template_id = template.baseline_start_task_id.id

        criteria = [
            ("project_id", "=", self.project_id.id),
            ("task_template_id", "=", task_template_id),
        ]
        return self.env["project.task"].search(criteria)[0]

    @api.multi
    def _get_baseline_start_project(self):
        self.ensure_one()
        template = self.task_template_id
        if template.start_schedule_base_on != "manual":
            return self.project_id
        else:
            return False

    @api.multi
    def _get_baseline_finish_task(self):
        self.ensure_one()
        template = self.task_template_id
        if template.finish_schedule_base_on not in ["task_start", "task_finish"]:
            return False

        task_template_id = template.baseline_finish_task_id.id

        criteria = [
            ("project_id", "=", self.project_id.id),
            ("task_template_id", "=", task_template_id),
        ]
        return self.env["project.task"].search(criteria)[0]

    @api.multi
    def _get_baseline_finish_project(self):
        self.ensure_one()
        template = self.task_template_id
        if template.finish_schedule_base_on != "manual":
            return self.project_id
        else:
            return False

    @api.multi
    def _prepare_post_task_data(self):
        _super = super(ProjectTask, self)
        result = _super._prepare_post_task_data()

        if not self.task_template_id:
            return result

        template = self.task_template_id

        start_task = self._get_baseline_start_task()
        start_project = self._get_baseline_start_project()
        finish_task = self._get_baseline_finish_task()
        finish_project = self._get_baseline_finish_project()

        result.update(
            {
                "start_schedule_base_on": template.start_schedule_base_on,
                "finish_schedule_base_on": template.finish_schedule_base_on,
                "start_offset": template.start_offset,
                "finish_offset": template.finish_offset,
                "start_offset_uom_id": template.start_offset_uom_id
                and template.start_offset_uom_id.id
                or False,
                "finish_offset_uom_id": template.finish_offset_uom_id
                and template.finish_offset_uom_id.id
                or False,
                "baseline_start_task_id": start_task and start_task.id or False,
                "baseline_start_project_id": start_project
                and start_project.id
                or False,
                "baseline_finish_task_id": finish_task and finish_task.id or False,
                "baseline_finish_project_id": finish_project
                and finish_project.id
                or False,
            }
        )
        return result
