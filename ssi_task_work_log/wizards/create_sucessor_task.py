# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class CreateSucessorTaskDetail(models.TransientModel):
    _name = "create_sucessor_task_detail"
    _inherit = "create_sucessor_task_detail"

    def _compute_task_onchange(self, task_cache):
        _super = super(CreateSucessorTaskDetail, self)
        result = _super._compute_task_onchange(task_cache)
        result.onchange_work_estimation()
        return result
