# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Template - Baseline Integration",
    "version": "8.0.1.1.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "project_task_template",
        "project_baseline",
    ],
    "data": [
        "views/project_template_views.xml",
        "views/project_task_template_views.xml",
    ],
}
