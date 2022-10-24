# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectIssue(models.Model):
    _inherit = "project.issue"

    @api.depends(
        "task_ids",
        "task_ids.stage_id",
        "task_ids.state",
    )
    def _compute_task(self):
        for record in self:
            task_count = (
                task_no_state_count
            ) = (
                task_draft_count
            ) = task_open_count = task_done_count = task_pending_count = 0
            task_done = False
            if record.task_ids:
                for task in record.task_ids:
                    task_count += 1
                    if task.state == "draft":
                        task_draft_count += 1
                    elif task.state == "open":
                        task_open_count += 1
                    elif task.state == "done":
                        task_done_count += 1
                    elif task.state == "pending":
                        task_pending_count += 1
                    else:
                        task_no_state_count += 1
                if task_count == task_done_count:
                    task_done = True
            record.task_count = task_count
            record.task_draft_count = task_draft_count
            record.task_open_count = task_open_count
            record.task_done_count = task_done_count
            record.task_no_state_count = task_no_state_count
            record.task_pending_count = task_pending_count
            record.task_done = task_done

    task_count = fields.Integer(
        string="Task Count",
        compute="_compute_task",
        store=True,
    )
    task_draft_count = fields.Integer(
        string="Task Draft Count",
        compute="_compute_task",
        store=True,
    )
    task_open_count = fields.Integer(
        string="Task Open Count",
        compute="_compute_task",
        store=True,
    )
    task_done_count = fields.Integer(
        string="Task Done Count",
        compute="_compute_task",
        store=True,
    )
    task_pending_count = fields.Integer(
        string="Task Pending Count",
        compute="_compute_task",
        store=True,
    )
    task_no_state_count = fields.Integer(
        string="Task No State Count",
        compute="_compute_task",
        store=True,
    )
    task_done = fields.Boolean(
        string="Task Done",
        compute="_compute_task",
        store=True,
    )
