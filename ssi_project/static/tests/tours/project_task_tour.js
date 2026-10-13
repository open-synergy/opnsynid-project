/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_task_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    /**
     * Steps that open the Project > Tasks menu.
     * Tasks is a leaf of the Project app, so one click opens its list.
     */
    function openTaskMenuSteps() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Project app",
                trigger: '.o_app[data-menu-xmlid="project.menu_main_pm"]',
            },
            {
                content: "Open the Tasks menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="project.menu_project_management"]',
            },
            {
                content: "Tasks list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Tasks)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/project_task/01-create.md
    tour.register(
        "ssi_project_project_task_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Tasks menu.
            openTaskMenuSteps(),
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
                    content: "Enter the task title",
                    trigger: ".o_field_widget[name='name']",
                    run: "text TOUR-TASK-CREATE",
                },
                {
                    content: "Select the project",
                    trigger: ".o_field_many2one[name='project_id'] input",
                    run: "text TOUR-TASK-PROJECT",
                },
                {
                    content: "Pick the project from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR-TASK-PROJECT)",
                    in_modal: false,
                },
                // ── Flow 4 — Assign to Me is conditional (the assignee defaults
                // to the current user), so the tour does not click it.
                // ── Flow 5 — Click Save.
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
                // ── Post-Condition — The default stage is highlighted.
                {
                    content: "The default stage is highlighted",
                    trigger:
                        ".o_statusbar_status .o_arrow_button.btn-primary:contains(TOUR-TASK-STAGE-A)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/project_task/15-change-stage.md
    tour.register(
        "ssi_project_project_task_change_stage",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Tasks menu.
            openTaskMenuSteps(),
            [
                // ── Flow 2 — Find and open the record.
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(TOUR-TASK-CHANGE) .o_data_cell:contains(TOUR-TASK-CHANGE)",
                    extra_trigger: ".o_list_view",
                },
                {
                    trigger: ".o_form_view",
                    run: function () {
                        // Assertion only.
                    },
                },
                // ── Flow 3 — Click the target stage in the stage bar.
                {
                    content: "Click the target stage",
                    trigger:
                        ".o_statusbar_status .o_arrow_button:contains(TOUR-TASK-STAGE-B)",
                    extra_trigger: ".o_form_view",
                },
                // ── Post-Condition — The clicked stage is highlighted.
                {
                    content: "The clicked stage is highlighted",
                    trigger:
                        ".o_statusbar_status .o_arrow_button.btn-primary:contains(TOUR-TASK-STAGE-B)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );
});
