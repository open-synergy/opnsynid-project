# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Task Quality Control",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_stage_state",
        "project_task_category_view",
        "base_action_rule",
        "base_ir_filters_active",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_filters_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_action_rule_data.xml",
        "views/project_category_main_views.xml",
        "views/project_task_views.xml",
        "views/project_category_main_qc_question_views.xml",
    ],
}
