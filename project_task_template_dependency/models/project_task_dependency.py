# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ProjectTaskTemplateDependency(models.Model):
    _name = "project.task_template_dependency"
    _descrption = "Project Task Template Dependency"

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task_template",
        required=True,
        ondelete="restrict",
    )
    predecessor_task_id = fields.Many2one(
        string="Predecessor Task",
        comodel_name="project.task_template",
        required=True,
        ondelete="restrict",
    )
    dependency_type = fields.Selection(
        string="Dependency Type",
        selection=[
            ("start_finish", "Start-To-Finish"),
            ("start_start", "Start-To-Start"),
            ("finish_start", "Finish-To-Start"),
            ("finish_finish", "Finish-To-Finish"),
        ],
        required=True,
    )

    @api.constrains(
        "task_id",
        "predecessor_task_id",
    )
    def check_no_same_task(self):
        if self.task_id == self.predecessor_task_id:
            raise UserError(_("You can not select itself for predecessor/sucessor"))
