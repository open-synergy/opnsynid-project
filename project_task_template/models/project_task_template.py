# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields


class ProjectTaskTemplate(models.Model):
    _name = "project.task_template"
    _inherit = ["mail.thread"]
    _descrption = "Project Task Template"

    name = fields.Char(
        string="Template Name",
        required=True,
    )
    project_template_id = fields.Many2one(
        string="Project Template",
        comodel_name="project.template",
        required=True,
    )
    user_id = fields.Many2one(
        string="Assigned To",
        comodel_name="res.users",
    )
    reviewer_id = fields.Many2one(
        string="Reviewer",
        comodel_name="res.users",
    )
    planned_hours = fields.Float(
        string="Planned Hours",
    )
    active = fields.Boolean(
        string="Active",
        required=True,
        default=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=True,
    )
    note = fields.Text(
        string="Note",
    )

    @api.multi
    def _prepare_task_data(self, project_id):
        self.ensure_one()
        return {
            "name": self.name,
            "sequence": self.sequence,
            "user_id": self.user_id and
            self.user_id.id or False,
            "reviewer_id": self.reviewer_id and
            self.reviewer_id.id or False,
            "task_template_id": self.id,
            "project_id": project_id,
            "planned_hours": self.planned_hours,
        }
