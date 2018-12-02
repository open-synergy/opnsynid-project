# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Template",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_template_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
    ],
}
