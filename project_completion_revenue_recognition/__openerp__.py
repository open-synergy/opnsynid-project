# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Recognize Revenue When Project Complete",
    "version": "8.0.1.0.2",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_task_template",
        "account_accountant",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_project_views.xml",
        "views/project_template_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
