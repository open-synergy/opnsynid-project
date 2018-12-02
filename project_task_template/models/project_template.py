# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields, _


class ProjectTemplate(models.Model):
    _name = "project.template"
    _inherit = ["mail.thread"]
    _descrption = "Project Template"

    @api.model
    def _privacy_visibility_selection_selection(self):
        return [
            ("public", _("Public project")),
            ("employees", _("Internal project: all employees can access")),
            ("followers", _("Private project: followers Only")),
        ]

    name = fields.Char(
        string="Template Name",
        required=True,
    )
    project_parent_id = fields.Many2one(
        string="Parent Project",
        comodel_name="account.analytic.account",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        required=True,
        default=True,
    )
    task_type_ids = fields.Many2many(
        string="Task Stages",
        comodel_name="project.task.type",
        relation="rel_project_template_2_task_type",
        column1="project_id",
        column2="stage_id",
    )
    privacy_visibility = fields.Selection(
        string="Privacy Visibility",
        selection=lambda self: self._privacy_visibility_selection_selection(),
        required=True,
    )
    task_template_ids = fields.One2many(
        string="Task Templates",
        comodel_name="project.task_template",
        inverse_name="project_template_id",
    )
    note = fields.Text(
        string="Note",
    )

    @api.multi
    def create_project(self):
        self.ensure_one()
        obj_project = self.env["project.project"]
        project = obj_project.create(
            self._prepare_project_data(),
        )
        for task_template in self.task_template_ids:
            self.env["project.task"].create(
                task_template._prepare_task_data(project.id)
            )
        for task in project.tasks:
            task.write(
                task._prepare_post_task_data()
            )
        return self._prepare_open_project(project)

    @api.multi
    def _prepare_project_data(self):
        self.ensure_one()
        return {
            "name": self.name,
            "privacy_visibility": self.privacy_visibility,
            "project_template_id": self.id,
            "type_ids": [(6, 0, self.task_type_ids.ids)],
            "active": True,
        }

    @api.multi
    def _prepare_open_project(self, project):
        self.ensure_one()
        return {
            "name": project.name,
            "type": "ir.actions.act_window",
            "res_model": "project.project",
            "view_type": "form",
            "view_mode": "form",
            "res_id": project.id,
        }
