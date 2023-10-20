# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project Extension",
    "version": "14.0.2.14.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_stage_state",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_model_access_data.xml",
        "security/ir_rule_data.xml",
        "menu.xml",
        "wizards/create_sucessor_task.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "views/project_task_type_views.xml",
        "views/project_tags_views.xml",
        "views/mail_activity_type_views.xml",
    ],
    "demo": [],
}
