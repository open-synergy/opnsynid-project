# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Task Custom Information",
    "version": "8.0.1.0.0",
    "author": "PT. Simetri Sinergi Indonesia,OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_task_category_view",
        "base_custom_information",
    ],
    "data": [
        "views/project_task_custom_information_views.xml",
        "views/project_category_main_views.xml"
    ],
}
