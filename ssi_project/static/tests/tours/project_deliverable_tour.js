/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_project.project_deliverable_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    /**
     * Steps that open the Project > Project > Deliverables menu.
     * "Project" (level 2) is a section without action: its step only opens the
     * dropdown that holds the Deliverables leaf.
     */
    function openMenuSteps() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Project app",
                trigger: '.o_app[data-menu-xmlid="project.menu_main_pm"]',
            },
            {
                content: "Open the Project menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_project.menu_project_root_menu"]',
            },
            {
                content: "Open the Deliverables menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_project.menu_project_deliverable"]',
            },
            {
                content: "Project Deliverables list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Project Deliverables)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    /**
     * Steps that open a record from the list.
     *
     * @param {String} name unique title of the record
     * @returns {Array} tour steps
     */
    function openRecordSteps(name) {
        return [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(" +
                    name +
                    ") .o_data_cell:contains(" +
                    name +
                    ")",
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

    // IK: docs/project_deliverable/01-create.md
    tour.register(
        "ssi_project_project_deliverable_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Project > Deliverables menu.
            openMenuSteps(),
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
                    run: "text TOURDL-NEWPROJECT",
                },
                {
                    content: "Pick the project from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOURDL-NEWPROJECT)",
                    in_modal: false,
                },
                {
                    content: "Select the Group/Single?",
                    trigger: "select.o_field_widget[name='ttype']",
                    run: "text Single Deliverable",
                },
                {
                    content: "Select the category",
                    trigger: ".o_field_many2one[name='category_id'] input",
                    run: "text TOURDL-CATEGORY",
                },
                {
                    content: "Pick the category from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOURDL-CATEGORY)",
                    in_modal: false,
                },
                {
                    content: "Select the type",
                    trigger: ".o_field_many2one[name='type_id'] input",
                    run: "text TOURDL-TYPE",
                },
                {
                    content: "Pick the type from the dropdown",
                    trigger: ".ui-autocomplete .ui-menu-item a:contains(TOURDL-TYPE)",
                    in_modal: false,
                },
                {
                    content: "Enter the title",
                    trigger: ".o_field_widget[name='title']",
                    run: "text TOURDL-NEW",
                },
                {
                    content: "Enter the Date Due",
                    trigger: ".o_field_widget[name='date_due'] input",
                    run: "text 12/31/2026",
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

    // IK: docs/project_deliverable/04-confirm.md
    tour.register(
        "ssi_project_project_deliverable_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Project > Deliverables menu.
            openMenuSteps(),
            // ── Flow 2 — Open the record.
            openRecordSteps("TOURDL-CONFIRM"),
            // ── Flow 3-4 — Click Confirm, click OK, check the status.
            actionSteps("action_confirm", "Confirm", "confirm")
        )
    );

    // IK: docs/project_deliverable/05-approve.md
    tour.register(
        "ssi_project_project_deliverable_approve",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Project > Deliverables menu.
            openMenuSteps(),
            // ── Flow 2 — Open the record.
            openRecordSteps("TOURDL-APPROVE"),
            // ── Flow 3-4 — Click Approve, click OK, check the status.
            actionSteps("action_approve_approval", "Approve", "open")
        )
    );

    // IK: docs/project_deliverable/09-finish.md
    tour.register(
        "ssi_project_project_deliverable_finish",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Project > Deliverables menu.
            openMenuSteps(),
            // ── Flow 2 — Open the record.
            openRecordSteps("TOURDL-FINISH"),
            // ── Flow 3-4 — Click Done, click OK, check the status.
            actionSteps("action_done", "Done", "done")
        )
    );

    // IK: docs/project_deliverable/10-cancel.md
    tour.register(
        "ssi_project_project_deliverable_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Project > Project > Deliverables menu.
            openMenuSteps(),
            // ── Flow 2 — Open the record to cancel.
            openRecordSteps("TOURDL-CANCEL"),
            [
                // ── Flow 3 — Click the Cancel button. It is a type="action"
                // button: its name is a numeric id in the DOM, so it is
                // targeted by label.
                {
                    content: "Click the Cancel button",
                    trigger: ".o_statusbar_buttons button:enabled:contains('Cancel')",
                    extra_trigger: ".o_form_view",
                },
                // ── Flow 4 — Select the Cancel Reason (radio widget).
                {
                    content: "Select the Cancel Reason",
                    trigger:
                        ".o_field_widget[name='cancel_reason_id'] .o_radio_item:contains(Tour Deliverable Cancel Reason) input",
                    in_modal: true,
                },
                // ── Flow 5 — Click Confirm in the wizard.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },
                // ── Flow 6 — Click OK on the stacked confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },
                // ── Post-Condition — Status changes to Cancelled.
                {
                    content: "Status is Cancelled",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                    extra_trigger: "body:not(:has(.modal))",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );
});
