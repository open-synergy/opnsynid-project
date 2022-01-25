# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    review_planned_hours = fields.Float(string="Initially Planned Review Hours")

    @api.depends(
        "effective_hours",
        "planned_hours",
        "review_planned_hours",
    )
    @api.multi
    def _compute_remaining_hours(self):
        for document in self:
            remaining_hours = (
                document.planned_hours + document.review_planned_hours
            ) - document.effective_hours
            document.remaining_hours = remaining_hours

    remaining_hours = fields.Float(
        string="Remaining Hours",
        compute="_compute_remaining_hours",
        store=True,
    )
