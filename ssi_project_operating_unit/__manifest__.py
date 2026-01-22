# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project + Operating Unit",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_project",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/project_project.xml",
        "security/res_group/project_task.xml",
        "security/ir_rule/project_project.xml",
        "security/ir_rule/project_task.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": [],
}
