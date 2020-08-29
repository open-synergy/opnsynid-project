# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Generate Accrue Income Expense from Task",
    "version": "8.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "project_task_code",
        "project_onchange",
        "account_accountant",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/project_task_views.xml",
        "views/project_project_views.xml",
        "views/project_task_accrue_account_policy_views.xml",
        "views/project_task_accrue_qty_policy_views.xml",
        "views/project_task_accrue_price_policy_views.xml",
        "views/project_task_accrue_journal_policy_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
