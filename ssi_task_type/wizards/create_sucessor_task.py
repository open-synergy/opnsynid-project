# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CreateSucessorTaskDetail(models.TransientModel):
    _name = "create_sucessor_task_detail"
    _inherit = "create_sucessor_task_detail"
    _description = "Create Sucessor Tasks - Detail"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="task.type",
    )

    def _prepare_task_creation_value(self):
        _super = super(CreateSucessorTaskDetail, self)
        result = _super._prepare_task_creation_value()
        result.update(
            {
                "type_id": self.type_id and self.type_id.id or False,
            }
        )
        return result
