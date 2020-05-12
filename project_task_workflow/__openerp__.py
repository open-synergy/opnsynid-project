# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Task Workflow",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_workflow_policy",
    ],
    "data": [
        "data/base_workflow_policy_data.xml",
        "views/project_template_views.xml",
        "views/project_project_view.xml",
        "views/project_task_type_view.xml",
    ],
}
