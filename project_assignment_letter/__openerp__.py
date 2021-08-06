# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author/

{
    "name": "Project Assignment Letter",
    "version": "8.0.1.0.0",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "license": "AGPL-3",
    "depends": [
        "base_sequence_configurator",
        "base_workflow_policy",
        "base_print_policy",
        "base_multiple_approval",
        "base_cancel_reason",
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/ir_module_category_data.xml",
        "security/res_groups_data.xml",
        "data/base_cancel_reason_configurator_data.xml",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "views/project_assignment_letter_views.xml",
    ],
    "installable": True,
}
