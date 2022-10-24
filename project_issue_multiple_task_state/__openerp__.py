# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Project Issue Multiple Task - Task State",
    "version": "8.0.1.1.0",
    "author": "PT. Simetri Sinergi Indonesia,OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "category": "Project Management",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_issue_multiple_task",
        "project_stage_state",
    ],
    "data": [
        "views/project_issue_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
