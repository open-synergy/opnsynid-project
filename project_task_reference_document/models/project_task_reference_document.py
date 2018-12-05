# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectTaskReferenceDocument(models.Model):
    _name = "project.task_reference_document"
    _descrption = "Project Task Reference Document"

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
        required=True,
        ondelete="restrict",
    )
    type_id = fields.Many2one(
        string="Document Type",
        comodel_name="project.reference_document_type",
        required=True,
    )
    attachment_id = fields.Many2one(
        string="Attachment",
        comodel_name="ir.attachment",
        required=True,
    )
