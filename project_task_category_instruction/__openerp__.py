# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Task Category Instructions",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_task_category_view",
        "web_widget_url_listview",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_category_main_views.xml",
        "views/project_task_views.xml",
    ],
}
