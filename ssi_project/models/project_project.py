# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

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
