# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Template - Dependency Integration",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
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
    ],
}
