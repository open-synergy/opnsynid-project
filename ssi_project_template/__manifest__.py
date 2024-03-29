# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project and Task Template",
    "version": "14.0.2.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_project_type",
        "ssi_task_type",
        "ssi_task_timebox",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "views/project_template_views.xml",
        "views/task_template_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": [
        "demo/task_template_demo.xml",
        "demo/project_template_demo.xml",
    ],
}
