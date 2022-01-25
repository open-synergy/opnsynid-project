# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Template - Dependency Integration",
    "version": "8.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "project_task_template",
        "project_task_activity_dependency",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_template_views.xml",
        "views/project_task_template_views.xml",
    ],
}
