# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    assignment_letter_id = fields.Many2one(
        string="Assignment Letter",
        comodel_name="project.assignment_letter",
        readonly=True,
    )
