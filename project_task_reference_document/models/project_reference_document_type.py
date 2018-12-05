# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectReferenceDocumentType(models.Model):
    _name = "project.reference_document_type"
    _descrption = "Project Reference Document Type"

    name = fields.Char(
        string="Reference Document Type",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
