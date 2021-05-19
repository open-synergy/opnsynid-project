# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    task_ids = fields.Many2many(
        string="Tasks",
        comodel_name="project.task",
        relation="project_issues_tasks_rel",
        column1="issue_id",
        column2="task_id",
    )
