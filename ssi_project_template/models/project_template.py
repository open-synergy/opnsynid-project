# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectTemplate(models.Model):
    _name = "project.template"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Project Template"

    task_template_ids = fields.Many2many(
        string="Task Templates",
        comodel_name="task.template",
        relation="rel_project_template_2_task_template",
        column1="project_template_id",
        column2="task_template_id",
    )
    parent_id = fields.Many2one(
        string="Parent",
        comodel_name="project.template",
    )
    type_id = fields.Many2one(
        string="Project Type",
        comodel_name="project.type",
    )
