/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_milestone_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    /**
     * Steps that open the Project > Configuration > Project > Milestones menu.
     * "Project" (level 3) is a grouping header without action, so it has no step.
     */
    function openMilestoneMenuSteps() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Project app",
                trigger: '.o_app[data-menu-xmlid="project.menu_main_pm"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="project.menu_project_config"]',
            },
            {
                content: "Open the Milestones menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_project.menu_project_milestone"]',
            },
            {
                content: "Project Milestones list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Project Milestones)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/project_milestone/01-create.md
    tour.register(
        "ssi_project_project_milestone_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Configuration > Project > Milestones menu.
            openMilestoneMenuSteps(),
            [
                // ── Flow 2 — Click the New button.
                {
                    content: "Click Create",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only.
                    },
                },
                // ── Flow 3 — Fill in the required fields.
                {
                    content: "Select the project",
                    trigger: ".o_field_many2one[name='project_id'] input",
                    run: "text TOUR-MS-PROJECT",
                },
                {
                    content: "Pick the project from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR-MS-PROJECT)",
                    in_modal: false,
                },
                {
                    content: "Select the phase",
                    trigger: ".o_field_many2one[name='phase_id'] input",
                    run: "text TOUR-MS-PHASE",
                },
                {
                    content: "Pick the phase from the dropdown",
                    trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-MS-PHASE)",
                    in_modal: false,
                },
                {
                    content: "Check Reporting Point",
                    trigger: ".o_field_widget[name='is_reporting_point'] input",
                    run: function () {
                        this.$anchor[0].click();
                    },
                },
                {
                    content: "Enter the Reporting Date",
                    trigger: ".o_field_widget[name='reporting_date'] input",
                    run: "text 03/31/2026",
                },
                // ── Flow 4 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only.
                    },
                },
                // ── Post-Condition — A new record is created in Draft status.
                {
                    content: "Status is Draft",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/project_milestone/02-edit.md
    tour.register(
        "ssi_project_project_milestone_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Configuration > Project > Milestones menu.
            openMilestoneMenuSteps(),
            [
                // ── Flow 2 — Find and open the record to edit.
                {
                    content: "Open the record",
                    trigger: ".o_data_row:contains(TOUR-MS-EDIT) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        // Assertion only.
                    },
                },
                // ── Flow 3 — Click the Edit button.
                {
                    content: "Click the Edit button",
                    trigger: ".o_form_button_edit",
                },
                {
                    content: "Form is now editable",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only.
                    },
                },
                // ── Flow 4 — Change the required fields.
                {
                    content: "Check Reporting Point",
                    trigger: ".o_field_widget[name='is_reporting_point'] input",
                    run: function () {
                        this.$anchor[0].click();
                    },
                },
                {
                    content: "Enter the Reporting Date",
                    trigger: ".o_field_widget[name='reporting_date'] input",
                    run: "text 06/30/2026",
                },
                // ── Flow 5 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                // ── Post-Condition — The record is updated with the new values.
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/project_milestone/03-delete.md
    tour.register(
        "ssi_project_project_milestone_delete",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Configuration > Project > Milestones menu.
            openMilestoneMenuSteps(),
            [
                // ── Flow 2 — Find and open the record to delete.
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR-MSD-PROJECT) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        // Assertion only.
                    },
                },
                // ── Flow 3 — Click the Action menu, then click Delete.
                {
                    content: "Open the Action menu",
                    trigger: ".o_cp_action_menus button:contains(Action)",
                },
                {
                    content: "Click Delete",
                    trigger: ".o_cp_action_menus .o_menu_item a",
                    run: function () {
                        var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                            function () {
                                return $(this).text().trim() === "Delete";
                            }
                        );
                        $delete[0].click();
                    },
                },
                // ── Flow 4 — Click OK on the confirmation dialog.
                {
                    content: "Confirm deletion",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                // ── Flow 5 — Click Project Milestones in the breadcrumb.
                {
                    content: "Click the list breadcrumb to return to the list",
                    trigger:
                        ".breadcrumb-item.o_back_button a:contains(Project Milestones)",
                    extra_trigger: "body:not(:has(.modal))",
                },
                // ── Post-Condition — The record is removed from the list.
                {
                    content: "The deleted record is gone from the list",
                    trigger:
                        ".o_list_view:not(:has(.o_data_row:contains(TOUR-MSD-PROJECT)))",
                    extra_trigger: ".o_data_row",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );
});
