# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectBatchAssignmentAssignee(models.Model):
    _name = "project.batch_assignment_assignee"
    _description = "Project Batch Assignment Asignee"
    _order = "sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    batch_id = fields.Many2one(
        string="# Batch",
        comodel_name="project.batch_assignment",
        required=True,
        ondelete="cascade",
    )
    assignee_id = fields.Many2one(
        string="Assignee",
        comodel_name="res.users",
        required=True,
    )
    role_id = fields.Many2one(
        string="Role",
        comodel_name="project.role",
        required=True,
    )
    assignment_id = fields.Many2one(
        string="# Assignment",
        comodel_name="project.assignment",
        readonly=True,
    )

    def _create_project_assignment(self):
        self.ensure_one()
        if self.assignment_id:
            return True

        ProjectAssignment = self.env["project.assignment"]
        assignment = ProjectAssignment.create(self._prepare_create_project_assignment())
        self.write(
            {
                "assignment_id": assignment.id,
            }
        )

    def _update_project_assignment(self):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.write(self._prepare_update_project_assignment())

    def _prepare_create_project_assignment(self):
        self.ensure_one()
        batch = self.batch_id
        return {
            "project_id": batch.project_id.id,
            "asignee_id": self.assignee_id.id,
            "role_id": self.role_id.id,
            "date_start": batch.date_start,
            "date_end": batch.date_end,
            "date_assign": batch.date_assign,
            "batch_id": batch.id,
        }

    def _prepare_update_project_assignment(self):
        self.ensure_one()
        batch = self.batch_id
        return {
            "project_id": batch.project_id.id,
            "asignee_id": self.assignee_id.id,
            "role_id": self.role_id.id,
            "date_start": batch.date_start,
            "date_end": batch.date_end,
            "date_assign": batch.date_assign,
            "batch_id": batch.id,
        }

    def _confirm_project_assignment(self):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.action_confirm()

    def _open_project_assignment(self):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.action_open()

    def _done_project_assignment(self):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.action_done()

    def _restart_project_assignment(self):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.action_restart()

    def _cancel_project_assignment(self, cancel_reason=False):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.action_cancel(cancel_reason=cancel_reason)

    def _terminate_project_assignment(self, terminate_reason=False):
        self.ensure_one()
        if not self.assignment_id:
            return True

        self.assignment_id.action_terminate(terminate_reason=terminate_reason)
