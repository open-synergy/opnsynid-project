# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class CreateSucessorTaskDetail(models.TransientModel):
    _name = "create_sucessor_task_detail"
    _inherit = "create_sucessor_task_detail"
    _description = "Create Sucessor Tasks - Detail"

    timebox_offset = fields.Integer(
        string="Timebox Offset",
        required=True,
    )

    def _prepare_task_creation_value(self):
        _super = super(CreateSucessorTaskDetail, self)
        result = _super._prepare_task_creation_value()
        timebox_ids = self._get_timebox_ids()
        result.update(
            {
                "type_id": self.type_id and self.type_id.id or False,
                "timebox_ids": [(6, 0, timebox_ids)],
            }
        )
        return result

    def _get_timebox_ids(self):
        self.ensure_one()
        result = []
        task = self.wizard_id.task_id
        if task.timebox_latest_id:
            reference_timebox = target_timebox = task.timebox_latest_id
            if self.timebox_offset > 0:
                target_timebox = reference_timebox.find_next(self.timebox_offset)
            elif self.timebox_offset < 0:
                target_timebox = reference_timebox.find_previous(
                    abs(self.timebox_offset)
                )
            result = [target_timebox.id]
        return result
