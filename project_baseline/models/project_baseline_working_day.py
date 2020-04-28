# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields


class ProjectBaselineWorkingDay(models.Model):
    _name = "project.baseline.working_day"
    _description = "Working Day for Project Baseline"

    code = fields.Char(
        string="Code",
    )
    name = fields.Char(
        string="Name",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
