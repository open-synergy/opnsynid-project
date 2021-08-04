# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    assignment_letter_sequence_id = fields.Many2one(
        string="Assignment Letter Sequence",
        comodel_name="ir.sequence",
        company_dependent=True,
    )
    assignment_letter_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Assignment Letter",
        comodel_name="res.groups",
        relation="rel_project_confirm_assigment_letter",
        column1="project_id",
        column2="group_id",
    )
    assignment_letter_restart_validation_grp_ids = fields.Many2many(
        string="Allow To Restart Validation Assignment Letter",
        comodel_name="res.groups",
        relation="rel_project_restart_validation_assigment_letter",
        column1="project_id",
        column2="group_id",
    )
    assignment_letter_cancel_grp_ids = fields.Many2many(
        string="Allow To Cancel Assignment Letter",
        comodel_name="res.groups",
        relation="rel_project_cancel_assigment_letter",
        column1="project_id",
        column2="group_id",
    )
    assignment_letter_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Assignment Letter",
        comodel_name="res.groups",
        relation="rel_project_restart_assigment_letter",
        column1="project_id",
        column2="group_id",
    )
