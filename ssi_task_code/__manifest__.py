# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Task Code",
    "version": "14.0.1.3.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "ssi_project",
        "ssi_sequence_mixin",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "views/project_task_views.xml",
    ],
    "demo": [],
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
}
