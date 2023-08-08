# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project Type",
    "version": "14.0.1.3.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_project",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "views/project_type_views.xml",
        "views/project_project_views.xml",
    ],
    "demo": [],
}
