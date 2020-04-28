# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Baseline",
    "version": "8.0.1.8.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project"
    ],
    "external_dependencies": {
        "python": [
            "pandas",
        ],
    },
    "data": [
        "security/ir.model.access.csv",
        "data/project_baseline_working_day_data.xml",
        "views/project_task_views.xml",
        "views/project_project_views.xml",
    ],
}
