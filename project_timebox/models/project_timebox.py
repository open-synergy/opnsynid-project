# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectTimebox(models.Model):
    _name = "project.timebox"
    _descrption = "Project Timebox"
    _order = "date_start, id"

    name = fields.Char(
        string="Timebox",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_stop = fields.Date(
        string="Date Stop",
        required=True,
    )
