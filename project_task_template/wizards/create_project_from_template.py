# -*- coding: utf-8 -*-
# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class CreateProjectFromTemplate(models.TransientModel):
    _name = "project.create_project_from_template"
    _description = "Create Project From Template"

    @api.model
    def _default_project_template_id(self):
        return self._context.get("active_id", False)

    name = fields.Char(
        string="Project Name",
    )
    partner_id = fields.Many2one(
        string="Customer",
        comodel_name="res.partner",
    )
    project_parent_id = fields.Many2one(
        string="Parent Project",
        comodel_name="account.analytic.account",
    )
    project_template_id = fields.Many2one(
        string="Project Template",
        comodel_name="project.template",
        default=lambda self: self._default_project_template_id(),
    )

    @api.multi
    def button_generate(self):
        self.ensure_one()
        return self.project_template_id.create_project(
            self.name or False,
            self.project_parent_id and self.project_parent_id.id or False,
            self.partner_id and self.partner_id.id or False,
        )
