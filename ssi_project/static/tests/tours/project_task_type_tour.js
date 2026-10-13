/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_task_type_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/project_task_type/01-create.md
    tour.register(
        "ssi_project_project_task_type_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Project > Configuration > Project > Stages menu.
            // "Configuration" (level 2) is a section: its step only opens the
            // dropdown. "Project" (level 3) is a header, so the leaf is clicked
            // directly.
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
                content: "Open the Stages menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="project.menu_project_config_project"]',
            },
            {
                content: "Stages list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Stages)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
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
                content: "Enter the stage name",
                trigger: ".o_field_widget[name='name']",
                run: "text TOUR-STAGE-CREATE",
            },
            {
                content: "Select the state",
                trigger: "select.o_field_widget[name='state']",
                run: "text In Progress",
            },
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
            // ── Post-Condition — The new stage exists.
            {
                content: "The new stage is shown",
                trigger: ".o_field_widget[name='name']:contains(TOUR-STAGE-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
