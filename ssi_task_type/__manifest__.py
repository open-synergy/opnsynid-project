# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Task Type",
    "version": "14.0.1.8.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "ssi_project",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "wizards/create_sucessor_task.xml",
        "views/task_type_views.xml",
        "views/task_type_category_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": [],
}
