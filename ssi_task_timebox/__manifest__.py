# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Task Timebox",
    "version": "14.0.4.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_project",
        "ssi_master_data_mixin",
        "ssi_duration_mixin",
        "base_automation",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
        "wizards/create_sucessor_task.xml",
        "views/task_timebox_views.xml",
        "views/project_task_views.xml",
        "views/project_project_views.xml",
    ],
    "demo": [],
}
