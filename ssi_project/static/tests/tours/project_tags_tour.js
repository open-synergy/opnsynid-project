/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_tags_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/project_tags/01-create.md
    tour.register(
        "ssi_project_project_tags_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Project > Configuration > Project > Tags menu.
            // "Configuration" (level 2) only opens the dropdown; the level 3
            // "Project" header is skipped and the leaf is clicked directly.
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
                content: "Open the Tags menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="project.menu_project_tags_act"]',
            },
            {
                content: "Tags list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Tags)",
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
                content: "Enter the tag name",
                trigger: ".o_field_widget[name='name']",
                run: "text TOUR-TAG-CREATE",
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
            // ── Post-Condition — The new tag exists.
            {
                content: "The new tag is shown",
                trigger: ".o_field_widget[name='name']:contains(TOUR-TAG-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
