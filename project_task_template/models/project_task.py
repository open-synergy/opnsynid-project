# -*- coding: utf-8 -*-
# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    task_template_id = fields.Many2one(
        string="Template",
        comodel_name="project.task_template",
    )

    @api.multi
    def _prepare_post_task_data(self):
        self.ensure_one()
        return {}
