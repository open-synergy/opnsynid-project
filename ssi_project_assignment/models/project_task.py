# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    @api.depends(
        "project_id",
        "user_id",
        "role_id",
    )
    def _compute_project_assignment_id(self):
        for rec in self:
            project_assignment_id = self.env["project.assignment"]
            if rec.project_id and rec.user_id and rec.role_id:
                project_assignment_id = self.env["project.assignment"].search(
                    [
                        ("project_id", "=", rec.project_id.id),
                        ("asignee_id", "=", rec.user_id.id),
                        ("role_id", "=", rec.role_id.id),
                        ("state", "not in", ["reject", "cancel"]),
                    ],
                    limit=1,
                )
            rec.project_assignment_id = project_assignment_id.id

    role_id = fields.Many2one(
        string="Role",
        comodel_name="project.role",
        ondelete="restrict",
    )
    project_assignment_id = fields.Many2one(
        comodel_name="project.assignment",
        string="Project Assignment",
        compute="_compute_project_assignment_id",
        compute_sudo=True,
        store=True,
    )

    @api.depends(
        "type_id",
        "role_id",
    )
    def _compute_allowed_assigned_ids(self):
        User = self.env["res.users"]
        for record in self:
            result = User.search([]).ids
            if record.type_id and self.role_id and self.type_id.restrict_assignment:
                result = (
                    record.project_id.active_assignment_ids.filtered(
                        lambda r: r.role_id.id == record.role_id.id
                    )
                    .mapped("asignee_id")
                    .ids
                )
            record.allowed_assigned_ids = result

    allowed_assigned_ids = fields.Many2many(
        string="Allowed Users",
        comodel_name="res.users",
        compute="_compute_allowed_assigned_ids",
        store=False,
    )

    @api.onchange(
        "type_id",
    )
    def onchange_role_id(self):
        self.role_id = False
        if self.type_id.role_id:
            self.role_id = self.type_id.role_id

    @api.onchange(
        "type_id",
        "role_id",
    )
    def onchange_user_id(self):
        self.user_id = False
