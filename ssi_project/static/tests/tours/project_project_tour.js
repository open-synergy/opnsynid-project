/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_project_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    /**
     * Steps that open the Project > Projects menu.
     * Projects is the landing menu of the Project app, so the click reloads the
     * same action: the control panel is marked first and the gate waits for the
     * unmarked (re-mounted) one.
     */
    function openProjectMenuSteps() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Project app",
                trigger: '.o_app[data-menu-xmlid="project.menu_main_pm"]',
            },
            {
                content: "Open the Projects menu",
                trigger: '.o_menu_sections [data-menu-xmlid="project.menu_projects"]',
                run: function (actions) {
                    // Instrumentation marker, destroyed with the old controller.
                    $(".o_control_panel").addClass("oe_tour_stale");
                    actions.click();
                },
            },
            {
                content: "Projects list is displayed",
                trigger: ".o_control_panel:not(.oe_tour_stale)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    /**
     * Steps that open a project from the list.
     *
     * @param {String} name unique project name
     * @returns {Array} tour steps
     */
    function openProjectSteps(name) {
        return [
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(" + name + ") .o_data_cell[name='name']",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    /**
     * Steps that click a header button, confirm the dialog and assert the state.
     *
     * @param {String} button technical name of the button
     * @param {String} label button label
     * @param {String} state expected state key
     * @returns {Array} tour steps
     */
    function actionSteps(button, label, state) {
        return [
            {
                content: "Click the " + label + " button",
                trigger: ".o_statusbar_buttons button[name='" + button + "']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status changed",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='" +
                    state +
                    "'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/project.project/01-create.md
    tour.register(
        "ssi_project_project_project_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Projects menu.
            openProjectMenuSteps(),
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
                {
                    content: "Enter the project name",
                    trigger: ".o_field_widget[name='name']",
                    run: "text TOUR-PRJ-CREATE",
                },
                // ── Flow 3 — On the Settings tab, select the Units.
                {
                    content: "Open the Settings tab",
                    trigger: ".o_notebook .nav-link:contains(Settings)",
                },
                {
                    content: "Select the unit",
                    trigger: ".o_field_many2manytags[name='unit_partner_ids'] input",
                    run: "text TOUR-UNIT-ORG",
                },
                {
                    content: "Pick the unit from the dropdown",
                    trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-UNIT-ORG)",
                    in_modal: false,
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
                // ── Post-Condition — The selected units are listed in Units.
                {
                    content: "The unit is listed in the Units field",
                    trigger:
                        ".o_field_many2manytags[name='unit_partner_ids'] .badge:contains(TOUR-UNIT-ORG)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/project.project/07-start.md
    tour.register(
        "ssi_project_project_project_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Projects menu.
            openProjectMenuSteps(),
            // ── Flow 2 — Open the record.
            openProjectSteps("TOUR-PRJ-START"),
            // ── Flow 3-4 — Click the Start button, click OK, check the status.
            actionSteps("action_confirm", "Start", "open")
        )
    );

    // IK: docs/project.project/15-pending.md
    tour.register(
        "ssi_project_project_project_pending",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Projects menu.
            openProjectMenuSteps(),
            // ── Flow 2 — Open the record.
            openProjectSteps("TOUR-PRJ-PENDING"),
            // ── Flow 3-4 — Click the Pending button, click OK, check the status.
            actionSteps("action_pending", "Pending", "pending")
        )
    );

    // IK: docs/project.project/09-finish.md
    tour.register(
        "ssi_project_project_project_finish",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Projects menu.
            openProjectMenuSteps(),
            // ── Flow 2 — Open the record.
            openProjectSteps("TOUR-PRJ-FINISH"),
            // ── Flow 3-4 — Click the Done button, click OK, check the status.
            actionSteps("action_done", "Done", "done")
        )
    );

    // IK: docs/project.project/10-cancel.md
    tour.register(
        "ssi_project_project_project_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Projects menu.
            openProjectMenuSteps(),
            // ── Flow 2 — Open the record.
            openProjectSteps("TOUR-PRJ-CANCEL"),
            // ── Flow 3-4 — Click the Cancel button, click OK, check the status.
            actionSteps("action_cancel", "Cancel", "cancel")
        )
    );

    // IK: docs/project.project/12-restart.md
    tour.register(
        "ssi_project_project_project_restart",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Projects menu.
            openProjectMenuSteps(),
            // ── Flow 2 — Open the record.
            openProjectSteps("TOUR-PRJ-RESTART"),
            // ── Flow 3-4 — Click the Restart button, click OK, check the status.
            actionSteps("action_draft", "Restart", "draft")
        )
    );
});
