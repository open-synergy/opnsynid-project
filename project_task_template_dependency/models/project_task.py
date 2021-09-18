# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    def _prepare_post_task_data(self):
        _super = super(ProjectTask, self)
        result = _super._prepare_post_task_data()

        if not self.task_template_id:
            return result

        template = self.task_template_id

        predecessors = []

        for predecessor in template.predecessor_ids:
            predecessor_task = self.project_id._get_task_from_template(
                predecessor.predecessor_task_id
            )
            predecessors.append(
                (
                    0,
                    0,
                    {
                        "task_id": self.id,
                        "predecessor_task_id": predecessor_task
                        and predecessor_task.id
                        or False,
                        "dependency_type": predecessor.dependency_type,
                    },
                )
            )

        result.update(
            {
                "predecessor_ids": predecessors,
            }
        )
        return result
