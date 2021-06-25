# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Issue Print Policy",
    "version": "8.0.1.0.0",
    "category": "Project Management",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "project_issue",
        "base_print_policy",
    ],
    "data": [
        "views/project_issue_views.xml",
    ],
}
