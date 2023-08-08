# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    assignment_ids = fields.One2many(
        string="Assignments",
        comodel_name="project.assignment",
        inverse_name="project_id",
    )
    active_assignment_ids = fields.One2many(
        string="Active Assignments",
        comodel_name="project.assignment",
        inverse_name="project_id",
        domain=[
            ("state", "=", "open"),
        ],
        readonly=True,
    )
    all_assignment_ids = fields.One2many(
        string="All Assignments",
        comodel_name="project.assignment",
        inverse_name="project_id",
        domain=[
            ("state", "in", ["open", "done", "terminate"]),
        ],
        readonly=True,
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
            ).mapped("asignee_id")
            result_active = record.assignment_ids.filtered(
                lambda r: r.state == "open"
            ).mapped("asignee_id")
            record.team_ids = result.ids
            record.active_team_ids = result_active.ids

    team_ids = fields.Many2many(
        string="Team(s)",
        comodel_name="res.users",
        relation="rel_project_to_team",
        column1="project_id",
        column2="user_id",
        compute="_compute_team_ids",
        store=True,
    )
    active_team_ids = fields.Many2many(
        string="Active Team(s)",
        comodel_name="res.users",
        relation="rel_project_to_active_team",
        column1="project_id",
        column2="user_id",
        compute="_compute_team_ids",
        store=True,
    )
