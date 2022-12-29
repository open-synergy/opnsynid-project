# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    role_id = fields.Many2one(
        string="Role",
        comodel_name="project.role",
        ondelete="restrict",
    )

    @api.depends(
        "type_id",
        "role_id",
    )
    def _compute_allowed_user_ids(self):
        User = self.env["res.users"]
        for record in self:
            result = User.search([]).ids
            if record.type_id and self.role_id and self.type_id.restrict_assignment:
                result = (
                    record.project_id.active_assignment_ids.filtered(
                        lambda r: r.role_id.id == record.role_id.id
                    )
                    .mapped("user_id")
                    .ids
                )
            record.allowed_user_ids = result

    allowed_user_ids = fields.Many2many(
        string="Allowed Users",
        comodel_name="res.users",
        compute="_compute_allowed_user_ids",
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
