# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project Assignment + Operating Unit",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_project_operating_unit",
        "ssi_project_assignment",
    ],
    "data": [
        "security/res_group/project_assignment.xml",
        "security/ir_rule/project_assignment.xml",
        "views/project_assignment_views.xml",
    ],
    "demo": [],
}
