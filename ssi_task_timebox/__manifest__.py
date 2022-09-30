# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Task Timebox",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "ssi_project",
        "ssi_master_data_mixin",
        "ssi_duration_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/task_timebox_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": [],
}