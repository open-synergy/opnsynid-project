# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).
{
    "name": "Task - Work Log Integration",
    "version": "14.0.1.8.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_task_type",
        "ssi_project_work_log",
        "ssi_work_log_mixin",
    ],
    "data": [
        "views/task_type_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": [],
    "images": [],
}
