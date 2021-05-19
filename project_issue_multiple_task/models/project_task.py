# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    issue_ids = fields.Many2many(
        string="Issues",
        comodel_name="project.issue",
        relation="project_issues_tasks_rel",
        column1="task_id",
        column2="issue_id",
    )
