# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class TaskDependency(models.Model):
    _name = "task.dependency"
    _inherit = "task.dependency"

    offset_from_predecessor = fields.Integer(
        string="Offset From Predecessor",
        default=0,
        required=True,
    )
    target_timebox_from_predecessor = fields.Many2one(
        string="Target Timebox From Predecessor",
        comodel_name="task.timebox",
        compute="_compute_target_timebox_from_predecessor",
        store=True,
    )

    @api.depends(
        "predecessor_task_id",
        "predecessor_task_id.timebox_latest_id",
        "offset_from_predecessor",
    )
    def _compute_target_timebox_from_predecessor(self):
        for record in self:
            result = False
            if (
                record.predecessor_task_id
                and record.predecessor_task_id.timebox_latest_id
            ):
                result = record.predecessor_task_id.timebox_latest_id.find_next(
                    record.offset_from_predecessor
                )
            record.target_timebox_from_predecessor = result
