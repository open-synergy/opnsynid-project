# -*- coding: utf-8 -*-
# Copyright 2018-2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Template",
    "version": "8.0.1.3.1",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia,OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/create_project_from_template.xml",
        "views/project_task_template_views.xml",
        "views/project_template_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
