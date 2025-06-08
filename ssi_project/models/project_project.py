# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    @api.model
    def _default_type_ids(self):
        default_task_ids = self.env["project.task.type"].search(
            [("is_default", "=", True)]
        )
        return default_task_ids and default_task_ids.ids or []

    type_ids = fields.Many2many(
        default=lambda self: self._default_type_ids(),
    )

    milestone_ids = fields.One2many(
        string="Milestones",
        comodel_name="project_milestone",
        inverse_name="project_id",
    )
    deliverable_ids = fields.One2many(
        string="Deliverables",
        comodel_name="project_deliverable",
        inverse_name="project_id",
    )
    phase_ids = fields.One2many(
        string="Phases",
        comodel_name="project_phase",
        inverse_name="project_id",
    )
    num_of_milestone = fields.Integer(
        string="Num. of Milestone",
        compute="_compute_num_of_milestone",
        store=True,
        compute_sudo=True,
    )
    num_of_deliverable = fields.Integer(
        string="Num. of Deliverable",
        compute="_compute_num_of_deliverable",
        store=True,
        compute_sudo=True,
    )
    num_of_phase = fields.Integer(
        string="Num. of Phase",
        compute="_compute_num_of_phase",
        store=True,
        compute_sudo=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "New"),
            ("open", "In Progress"),
            ("done", "Done"),
            ("pending", "Pending"),
            ("cancel", "Cancel"),
        ],
        default="draft",
        copy=False,
    )

    @api.depends(
        "milestone_ids",
        "milestone_ids.project_id",
    )
    def _compute_num_of_milestone(self):
        Milestone = self.env["project_milestone"]
        for record in self:
            result = 0
            criteria = [("project_id", "=", record.id)]
            result = Milestone.search_count(criteria)
            record.num_of_milestone = result

    @api.depends(
        "deliverable_ids",
        "deliverable_ids.project_id",
    )
    def _compute_num_of_deliverable(self):
        Deliverable = self.env["project_deliverable"]
        for record in self:
            result = 0
            criteria = [
                ("project_id", "=", record.id),
                ("state", "in", ["open", "done", "terminate"]),
            ]
            result = Deliverable.search_count(criteria)
            record.num_of_deliverable = result

    @api.depends(
        "phase_ids",
        "phase_ids.project_id",
    )
    def _compute_num_of_phase(self):
        Phase = self.env["project_phase"]
        for record in self:
            result = 0
            criteria = [
                ("project_id", "=", record.id),
                ("state", "in", ["open", "done", "terminate"]),
            ]
            result = Phase.search_count(criteria)
            record.num_of_phase = result

    def _prepare_confirm_data(self):
        return {"state": "open"}

    def action_confirm(self):
        for rec in self.filtered(lambda p: p.state == "draft"):
            rec.write(rec._prepare_confirm_data())

    def _prepare_done_data(self):
        return {"state": "done"}

    def action_done(self):
        for rec in self.filtered(lambda p: p.state in ["open", "pending"]):
            rec.write(rec._prepare_done_data())

    def _prepare_pending_data(self):
        return {"state": "pending"}

    def action_pending(self):
        for rec in self.filtered(lambda p: p.state == "open"):
            rec.write(rec._prepare_pending_data())

    def _prepare_cancel_data(self):
        return {"state": "cancel"}

    def action_cancel(self):
        for rec in self.filtered(
            lambda p: p.state in ["draft", "open", "pending", "done"]
        ):
            rec.write(rec._prepare_cancel_data())

    def _prepare_draft_data(self):
        return {"state": "draft"}

    def action_draft(self):
        for rec in self.filtered(lambda p: p.state == "cancel"):
            rec.write(rec._prepare_draft_data())

    def action_open_milestone(self):
        for record in self.sudo():
            result = record._open_milestone()
        return result

    def action_open_deliverable(self):
        for record in self.sudo():
            result = record._open_deliverable()
        return result

    def action_open_phase(self):
        for record in self.sudo():
            result = record._open_phase()
        return result

    def _open_milestone(self):
        self.ensure_one()
        waction = self.env.ref("ssi_project.project_milestone_action").read()[0]
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("id", "in", self.milestone_ids.ids)],
                "context": {
                    "default_project_id": self.id,
                },
            }
        )
        return waction

    def _open_phase(self):
        self.ensure_one()
        waction = self.env.ref("ssi_project.project_phase_action").read()[0]
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("id", "in", self.phase_ids.ids)],
                "context": {
                    "default_project_id": self.id,
                },
            }
        )
        return waction

    def _open_deliverable(self):
        self.ensure_one()
        waction = self.env.ref("ssi_project.project_deliverable_action").read()[0]
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("id", "in", self.deliverable_ids.ids)],
                "context": {
                    "default_project_id": self.id,
                },
            }
        )
        return waction
