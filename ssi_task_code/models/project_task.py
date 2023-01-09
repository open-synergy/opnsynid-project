# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import _, api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = [
        "project.task",
        "mixin.sequence",
    ]

    code = fields.Char(
        string="Code",
        required=True,
        default="/",
        readonly=True,
    )

    _sql_constraints = [
        ("project_task_unique_code", "UNIQUE (code)", _("The code must be unique!")),
    ]

    @api.model_create_multi
    def create(self, values):
        _super = super(ProjectTask, self)
        result = _super.create(values)
        result._create_sequence()
        return result

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        default["code"] = "/"
        return super().copy(default)

    def name_get(self):
        result = super().name_get()
        new_result = []
        for task in result:
            rec = self.browse(task[0])
            name = "[{}] {}".format(rec.code, task[1])
            new_result.append((rec.id, name))
        return new_result
