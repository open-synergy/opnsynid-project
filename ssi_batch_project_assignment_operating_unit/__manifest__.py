# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project Batch Assignment + Operating Unit",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_project_assignment_operating_unit",
        "ssi_batch_project_assignment",
    ],
    "data": [
        "security/res_group/batch_project_assignment.xml",
        "security/ir_rule/batch_project_assignment.xml",
        "views/batch_project_assignment_views.xml",
    ],
    "demo": [],
}
