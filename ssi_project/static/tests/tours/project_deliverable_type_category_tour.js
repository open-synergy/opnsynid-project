/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_deliverable_type_category_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/project_deliverable_type_category/01-create.md
    tour.register(
        "ssi_project_project_deliverable_type_category_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Project > Configuration > Project > Deliverable Type Categories menu.
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
                content: "Open the Deliverable Type Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_project.menu_project_deliverable_type_category"]',
            },
            {
                content: "Project Deliverable Type Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Project Deliverable Type Categories)",
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
                content: "Enter the name",
                trigger: ".o_field_widget[name='name']",
                run: "text TOURDC-NEW",
            },
            {
                content: "Enter the code",
                trigger: ".o_field_widget[name='code']",
                run: "text TOURDCCODE",
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
            // ── Post-Condition — The new record exists.
            {
                content: "The new record is shown",
                trigger: ".o_field_widget[name='name']:contains(TOURDC-NEW)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
