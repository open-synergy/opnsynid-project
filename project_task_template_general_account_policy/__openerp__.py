# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Template - General Account Policy Integration",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "project_task_template",
        "account_analytic_line_general_account_policy",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_template_views.xml",
        "views/project_project_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
