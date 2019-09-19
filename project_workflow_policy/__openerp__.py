# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Workflow Policy",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_task_template",
        "base_workflow_policy",
    ],
    "data": [
        "data/base_workflow_policy_data.xml",
        "views/project_template_views.xml",
        "views/project_project_views.xml",
    ],
}
