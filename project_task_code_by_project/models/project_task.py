# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def create(self, vals):
        obj_project = self.env["project.project"]
        project_id = vals.get("project_id", False)

        if project_id:
            criteria = [
                ("id", "=", project_id)
            ]
            project = obj_project.search(criteria)
            if project.task_sequence_id:
                sequence = self.env["ir.sequence"].\
                    next_by_id(
                        project.task_sequence_id.id)
                vals["code"] = sequence
        return super(ProjectTask, self).create(vals)
