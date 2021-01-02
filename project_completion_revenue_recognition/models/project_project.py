# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    @api.depends(
        "project_template_id",
    )
    @api.multi
    def _compute_cip_account_move_line_ids(self):
        obj_move_line = self.env["account.move.line"]
        for project in self:
            result = []
            if project.project_template_id:
                criteria = [
                    (
                        "account_id",
                        "in",
                        project.project_template_id.allowed_cip_account_ids.ids,
                    ),
                    ("analytic_account_id", "=", project.analytic_account_id.id),
                    ("debit", ">", 0.0),
                ]
                result = obj_move_line.search(criteria).ids
            project.cip_account_move_line_ids = result

    @api.depends(
        "project_template_id",
    )
    @api.multi
    def _compute_billing_cip_account_move_line_ids(self):
        obj_move_line = self.env["account.move.line"]
        for project in self:
            result = []
            if project.project_template_id:
                criteria = [
                    (
                        "account_id",
                        "in",
                        project.project_template_id.allowed_billing_cip_account_ids.ids,
                    ),
                    ("analytic_account_id", "=", project.analytic_account_id.id),
                    ("credit", ">", 0.0),
                ]
                result = obj_move_line.search(criteria).ids
            project.billing_cip_account_move_line_ids = result

    revenue_recognition_on_project_completion = fields.Boolean(
        string="Recognize Project When Project Close",
        default=False,
    )
    project_completion_entry_id = fields.Many2one(
        string="Project Completion Accounting Entry",
        comodel_name="account.move",
        readonly=True,
    )
    project_completion_journal_id = fields.Many2one(
        string="Project Completion Journal",
        comodel_name="account.journal",
    )
    project_completion_date = fields.Date(
        string="Project Completion Date",
    )
    cost_account_mapping_ids = fields.One2many(
        string="Cost Account Mapping",
        comodel_name="project.cost_account_mapping",
        inverse_name="project_id",
    )
    revenue_account_mapping_ids = fields.One2many(
        string="Revenue Account Mapping",
        comodel_name="project.revenue_account_mapping",
        inverse_name="project_id",
    )
    cip_account_move_line_ids = fields.Many2many(
        string="CIP Journal Item",
        comodel_name="account.move.line",
        compute="_compute_cip_account_move_line_ids",
        store=False,
    )
    billing_cip_account_move_line_ids = fields.Many2many(
        string="Billing on CIP Journal Item",
        comodel_name="account.move.line",
        compute="_compute_billing_cip_account_move_line_ids",
        store=False,
    )

    @api.multi
    def set_done(self):
        _super = super(ProjectProject, self)
        _super.set_done()
        for project in self:
            project._create_project_completion_move()

    @api.multi
    def set_open(self):
        _super = super(ProjectProject, self)
        _super.set_open()
        for project in self:
            project._delete_project_completion_move()

    @api.multi
    def _delete_project_completion_move(self):
        self.ensure_one()
        move = self.project_completion_entry_id
        self.write({"project_completion_entry_id": False})
        if move:
            move.unlink()

    @api.multi
    def _create_project_completion_move(self):
        self.ensure_one()
        if self.revenue_recognition_on_project_completion:
            move = self.env["account.move"].create(
                self._prepare_project_completion_move()
            )
            self.write({"project_completion_entry_id": move.id})

    @api.multi
    def _get_project_completion_journal(self):
        self.ensure_one()
        journal = self.project_completion_journal_id
        error_msg = _("No project completion journal defined")

        if not journal and self.project_template_id:
            journal = self.project_template_id.project_completion_journal_id

        if not journal:
            raise UserError(error_msg)

        return journal

    @api.multi
    def _prepare_project_completion_move(self):
        self.ensure_one()
        entry_date = self.project_completion_date or fields.Date.today()
        period = self.env["account.period"].find(entry_date)
        expense_ml = []
        revenue_ml = []

        for expense_move in self.cip_account_move_line_ids:
            expense_ml.append(
                self._prepare_project_completion_expense_move_line(expense_move)
            )
            expense_ml.append(
                self._prepare_project_completion_cip_move_line(expense_move)
            )

        for revenue_move in self.billing_cip_account_move_line_ids:
            revenue_ml.append(
                self._prepare_project_completion_revenue_move_line(revenue_move)
            )
            revenue_ml.append(
                self._prepare_project_completion_billing_cip_move_line(revenue_move)
            )

        ml = expense_ml + revenue_ml

        return {
            "journal_id": self._get_project_completion_journal().id,
            "date": entry_date,
            "period_id": period.id,
            "ref": self.code,
            "line_id": ml,
        }

    @api.multi
    def _prepare_project_completion_expense_move_line(self, move_line):
        self.ensure_one()
        account = self._get_cost_from_cip_account(move_line.account_id)
        name = _("Project %s completion") % (self.code)
        return (
            0,
            0,
            {
                "name": name,
                "account_id": account.id,
                "debit": move_line.debit,
                "credit": 0.0,
                "analytic_account_id": self.analytic_account_id.id,
            },
        )

    @api.multi
    def _prepare_project_completion_cip_move_line(self, move_line):
        self.ensure_one()
        name = _("Project %s completion") % (self.code)
        return (
            0,
            0,
            {
                "name": name,
                "account_id": move_line.account_id.id,
                "debit": 0.0,
                "credit": move_line.debit,
                "analytic_account_id": self.analytic_account_id.id,
            },
        )

    @api.multi
    def _prepare_project_completion_revenue_move_line(self, move_line):
        self.ensure_one()
        account = self._get_revenue_from_billing_cip_account(move_line.account_id)
        name = _("Project %s completion") % (self.code)
        return (
            0,
            0,
            {
                "name": name,
                "account_id": account.id,
                "debit": 0.0,
                "credit": move_line.credit,
                "analytic_account_id": self.analytic_account_id.id,
            },
        )

    @api.multi
    def _prepare_project_completion_billing_cip_move_line(self, move_line):
        self.ensure_one()
        name = _("Project %s completion") % (self.code)
        return (
            0,
            0,
            {
                "name": name,
                "account_id": move_line.account_id.id,
                "debit": move_line.credit,
                "credit": 0.0,
                "analytic_account_id": self.analytic_account_id.id,
            },
        )

    @api.multi
    def _get_cost_from_cip_account(self, account):
        self.ensure_one()
        obj_project_cip_mapping = self.env["project.cost_account_mapping"]
        obj_project_template_cip_mapping = self.env[
            "project.template_cost_account_mapping"
        ]
        error_msg = _("No expense account defined")

        result = False

        criteria = [
            ("project_id", "=", self.id),
            ("cip_account_id", "=", account.id),
        ]

        mappings = obj_project_cip_mapping.search(criteria)

        if len(mappings) > 0:
            result = mappings[0].cost_account_id

        if not result and self.project_template_id:
            criteria = [
                ("project_template_id", "=", self.project_template_id.id),
                ("cip_account_id", "=", account.id),
            ]
            mappings = obj_project_template_cip_mapping.search(criteria)

            if len(mappings) > 0:
                result = mappings[0].cost_account_id

        if not result:
            raise UserError(error_msg)

        return result

    @api.multi
    def _get_revenue_from_billing_cip_account(self, account):
        self.ensure_one()
        obj_project_revenue_mapping = self.env["project.revenue_account_mapping"]
        obj_project_template_revenue_mapping = self.env[
            "project.template_revenue_account_mapping"
        ]
        error_msg = _("No revenue account defined")

        result = False

        criteria = [
            ("project_id", "=", self.id),
            ("billing_cip_account_id", "=", account.id),
        ]

        mappings = obj_project_revenue_mapping.search(criteria)

        if len(mappings) > 0:
            result = mappings[0].revenue_account_id

        if not result and self.project_template_id:
            criteria = [
                ("project_template_id", "=", self.project_template_id.id),
                ("billing_cip_account_id", "=", account.id),
            ]
            mappings = obj_project_template_revenue_mapping.search(criteria)

            if len(mappings) > 0:
                result = mappings[0].revenue_account_id

        if not result:
            raise UserError(error_msg)

        return result
