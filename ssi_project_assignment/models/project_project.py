# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    assignment_ids = fields.One2many(
        string="Assignments",
        comodel_name="project.assignment",
        inverse_name="project_id",
    )

    @api.depends(
        "assignment_ids",
        "assignment_ids.project_id",
        "assignment_ids.user_id",
        "assignment_ids.state",
    )
    def _compute_team_ids(self):
        for record in self:
            result = record.assignment_ids.filtered(
                lambda r: r.state in ["open", "done", "terminate"]
            ).mapped("user_id")
            record.team_ids = result.ids

    team_ids = fields.Many2many(
        string="Team(s)",
        comodel_name="res.users",
        relation="rel_project_to_team",
        column1="project_id",
        column2="user_id",
        compute="_compute_team_ids",
        store=True,
    )
