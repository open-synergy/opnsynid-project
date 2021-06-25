# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Print Policy",
    "version": "8.0.1.0.0",
    "category": "Project Management",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "project",
        "base_print_policy",
    ],
    "data": [
        "views/project_project_views.xml",
        "views/project_task_views.xml",
    ],
}
