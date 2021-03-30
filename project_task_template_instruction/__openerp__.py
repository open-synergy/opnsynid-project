# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Task Template Instructions",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_task_category_instruction",
        "project_task_template",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_task_views.xml",
        "views/project_task_template_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
