# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Task Document Reference",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_reference_document_type_views.xml",
        "views/project_task_views.xml",
    ],
}
