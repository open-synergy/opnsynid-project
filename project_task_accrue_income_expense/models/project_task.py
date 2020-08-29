# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, fields, _
from openerp.exceptions import Warning as UserError


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    @api.depends(
        "accrue_income_price_unit",
        "accrue_income_qty"
    )
    @api.multi
    def _compute_accrue_income_total(self):
        for document in self:
            result = document.accrue_income_price_unit * \
                document.accrue_income_qty
            document.accrue_income_total = result

    @api.depends(
        "accrue_expense_price_unit",
        "accrue_expense_qty"
    )
    @api.multi
    def _compute_accrue_expense_total(self):
        for document in self:
            result = document.accrue_expense_price_unit * \
                document.accrue_expense_qty
            document.accrue_expense_total = result

    accrue_expense_ok = fields.Boolean(
        string="Can Generate Accrue Expense",
        default=False,
    )
    accrue_expense_effective_date = fields.Date(
        string="Accrue Expense Effective Date",
    )
    accrue_expense_debit_account_policy_id = fields.Many2one(
        string="Accrue Expense Debit Account Policy",
        comodel_name="project.task_accrue_account_policy",
        ondelete="restrict",
    )
    accrue_expense_credit_account_policy_id = fields.Many2one(
        string="Accrue Expense Credit Account Policy",
        comodel_name="project.task_accrue_account_policy",
        ondelete="restrict",
    )
    accrue_expense_journal_policy_id = fields.Many2one(
        string="Accrue Expense Journal Policy",
        comodel_name="project.task_accrue_journal_policy",
        ondelete="restrict",
    )
    accrue_expense_qty_policy_id = fields.Many2one(
        string="Accrue Expense Qty Policy",
        comodel_name="project.task_accrue_qty_policy",
        ondelete="restrict",
    )
    accrue_expense_price_policy_id = fields.Many2one(
        string="Accrue Expense Price Policy",
        comodel_name="project.task_accrue_price_policy",
        ondelete="restrict",
    )
    accrue_expense_debit_account_id = fields.Many2one(
        string="Accrue Expense Debit Account",
        comodel_name="account.account",
        domain=[
            ("type", "not in", ["view", "consolidation", "closed"]),
        ],
        ondelete="restrict",
    )
    accrue_expense_credit_account_id = fields.Many2one(
        string="Accrue Expense Credit Account",
        comodel_name="account.account",
        domain=[
            ("type", "not in", ["view", "consolidation", "closed"]),
        ],
        ondelete="restrict",
    )
    accrue_expense_journal_id = fields.Many2one(
        string="Accrue Expense Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
        ondelete="restrict",
    )
    accrue_expense_move_id = fields.Many2one(
        string="# Accrue Expense",
        comodel_name="account.move",
        ondelete="restrict",
        readonly=True,
    )
    accrue_expense_price_unit = fields.Float(
        string="Accrue Expense Price Unit",
        default=0.0,
    )
    accrue_expense_qty = fields.Float(
        string="Accrue Expense Qty",
        default=0.0,
    )
    accrue_expense_uom_id = fields.Many2one(
        string="Accrue Expense UoM",
        comodel_name="product.uom",
        ondelete="restrict",
    )
    accrue_expense_total = fields.Float(
        string="Accrue Expense Total",
        compute="_compute_accrue_expense_total",
        store=True,
    )
    accrue_income_ok = fields.Boolean(
        string="Can Generate Accrue Income",
        default=False,
    )
    accrue_income_effective_date = fields.Date(
        string="Accrue Income Effective Date",
    )
    accrue_income_journal_policy_id = fields.Many2one(
        string="Accrue Income Journal Policy",
        comodel_name="project.task_accrue_journal_policy",
        ondelete="restrict",
    )
    accrue_income_debit_account_policy_id = fields.Many2one(
        string="Accrue Income Debit Account Policy",
        comodel_name="project.task_accrue_account_policy",
        ondelete="restrict",
    )
    accrue_income_credit_account_policy_id = fields.Many2one(
        string="Accrue Income Credit Account Policy",
        comodel_name="project.task_accrue_account_policy",
        ondelete="restrict",
    )
    accrue_income_qty_policy_id = fields.Many2one(
        string="Accrue Income Qty Policy",
        comodel_name="project.task_accrue_qty_policy",
        ondelete="restrict",
    )
    accrue_income_price_policy_id = fields.Many2one(
        string="Accrue Income Price Policy",
        comodel_name="project.task_accrue_price_policy",
        ondelete="restrict",
    )
    accrue_income_debit_account_id = fields.Many2one(
        string="Accrue Income Debit Account",
        comodel_name="account.account",
        domain=[
            ("type", "not in", ["view", "consolidation", "closed"]),
        ],
        ondelete="restrict",
    )
    accrue_income_credit_account_id = fields.Many2one(
        string="Accrue Income Credit Account",
        comodel_name="account.account",
        domain=[
            ("type", "not in", ["view", "consolidation", "closed"]),
        ],
        ondelete="restrict",
    )
    accrue_income_journal_id = fields.Many2one(
        string="Accrue Income Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
        ondelete="restrict",
    )
    accrue_income_move_id = fields.Many2one(
        string="# Accrue Income",
        comodel_name="account.move",
        ondelete="restrict",
        readonly=True,
    )
    accrue_income_price_unit = fields.Float(
        string="Accrue Income Price Unit",
        default=0.0,
    )
    accrue_income_qty = fields.Float(
        string="Accrue Income Qty",
        default=0.0,
    )
    accrue_income_uom_id = fields.Many2one(
        string="Accrue Income UoM",
        comodel_name="product.uom",
        ondelete="restrict",
    )
    accrue_income_total = fields.Float(
        string="Accrue Income Total",
        compute="_compute_accrue_income_total",
        store=True,
    )

    @api.multi
    def create_accrue_income_move(self):
        for document in self:
            document.write(self._create_accrue_income_move())

    @api.multi
    def delete_accrue_income_move(self):
        for document in self:
            move = self.accrue_income_move_id
            document.write(self._delete_accrue_income_move())
            move.unlink()

    @api.multi
    def create_accrue_expense_move(self):
        for document in self:
            document.write(self._create_accrue_expense_move())

    @api.multi
    def delete_accrue_expense_move(self):
        for document in self:
            move = self.accrue_expense_move_id
            document.write(self._delete_accrue_expense_move())
            move.unlink()

    @api.multi
    def _create_accrue_income_move(self):
        self.ensure_one()
        obj_move = self.env["account.move"]
        move = obj_move.create(self._prepare_accrue_income_move())
        return {
            "accrue_income_move_id": move.id,
        }

    @api.multi
    def _delete_accrue_income_move(self):
        self.ensure_one()
        return {
            "accrue_income_move_id": False,
        }

    @api.multi
    def _create_accrue_expense_move(self):
        self.ensure_one()
        obj_move = self.env["account.move"]
        move = obj_move.create(self._prepare_accrue_expense_move())
        return {
            "accrue_expense_move_id": move.id,
        }

    @api.multi
    def _delete_accrue_expense_move(self):
        self.ensure_one()
        return {
            "accrue_expense_move_id": False,
        }

    @api.multi
    def _prepare_move_lines(self, name, account_id, debit=0.0, credit=0.0):
        self.ensure_one()
        return {
            "name": name,
            "account_id": account_id,
            "debit": debit,
            "credit": credit,
            "analytic_account_id": self.project_id.analytic_account_id.id,
        }

    @api.multi
    def _prepare_accrue_income_move(self):
        self.ensure_one()
        entry_date = self.accrue_income_effective_date or fields.Date.today()
        period = self.env["account.period"].find(entry_date)
        return {
            "journal_id": self._get_accrue_income_journal().id,
            "date": entry_date,
            "period_id": period.id,
            "ref": self.code,
            "line_id": [
                (0, 0, self._prepare_accrue_income_debit_lines()),
                (0, 0, self._prepare_accrue_income_credit_lines()),
            ],
        }

    @api.multi
    def _get_accrue_income_journal(self):
        self.ensure_one()
        if not self.accrue_income_journal_id:
            error_msg = _("No accrue income journal defined")
            raise UserError(error_msg)

        return self.accrue_income_journal_id

    @api.multi
    def _prepare_accrue_income_debit_lines(self):
        self.ensure_one()
        name = _("%s accrue income" % self.code)
        return self._prepare_move_lines(
            name=name,
            account_id=self._get_accrue_income_debit_account().id,
            debit=self.accrue_income_total,
        )

    @api.multi
    def _prepare_accrue_income_credit_lines(self):
        self.ensure_one()
        name = _("%s accrue income" % self.code)
        return self._prepare_move_lines(
            name=name,
            account_id=self._get_accrue_income_credit_account().id,
            credit=self.accrue_income_total,
        )

    @api.multi
    def _get_accrue_income_debit_account(self):
        self.ensure_one()
        if not self.accrue_income_debit_account_id:
            error_msg = _("No accrue income debit account defined")
            raise UserError(error_msg)

        return self.accrue_income_debit_account_id

    @api.multi
    def _get_accrue_income_credit_account(self):
        self.ensure_one()
        if not self.accrue_income_credit_account_id:
            error_msg = _("No accrue income credit account defined")
            raise UserError(error_msg)

        return self.accrue_income_credit_account_id

    @api.multi
    def _prepare_accrue_expense_move(self):
        self.ensure_one()
        entry_date = self.accrue_expense_effective_date or fields.Date.today()
        period = self.env["account.period"].find(entry_date)
        return {
            "journal_id": self._get_accrue_expense_journal().id,
            "date": entry_date,
            "period_id": period.id,
            "ref": self.code,
            "line_id": [
                (0, 0, self._prepare_accrue_expense_debit_lines()),
                (0, 0, self._prepare_accrue_expense_credit_lines()),
            ],
        }

    @api.multi
    def _get_accrue_expense_journal(self):
        self.ensure_one()
        if not self.accrue_expense_journal_id:
            error_msg = _("No accrue expense journal defined")
            raise UserError(error_msg)

        return self.accrue_expense_journal_id

    @api.multi
    def _prepare_accrue_expense_debit_lines(self):
        self.ensure_one()
        name = _("%s accrue expense" % self.code)
        return self._prepare_move_lines(
            name=name,
            account_id=self._get_accrue_expense_debit_account().id,
            debit=self.accrue_expense_total,
        )

    @api.multi
    def _prepare_accrue_expense_credit_lines(self):
        self.ensure_one()
        name = _("%s accrue expense" % self.code)
        return self._prepare_move_lines(
            name=name,
            account_id=self._get_accrue_expense_credit_account().id,
            credit=self.accrue_expense_total,
        )

    @api.multi
    def _get_accrue_expense_debit_account(self):
        self.ensure_one()
        if not self.accrue_expense_debit_account_id:
            error_msg = _("No accrue expense debit account defined")
            raise UserError(error_msg)

        return self.accrue_expense_debit_account_id

    @api.multi
    def _get_accrue_expense_credit_account(self):
        self.ensure_one()
        if not self.accrue_expense_credit_account_id:
            error_msg = _("No accrue expense credit account defined")
            raise UserError(error_msg)

        return self.accrue_expense_credit_account_id

    @api.onchange(
        "accrue_expense_journal_policy_id",
    )
    def onchange_accrue_expense_journal_id(self):
        self.accrue_expense_journal_id = False
        if self.accrue_expense_journal_policy_id:
            result = self.accrue_expense_journal_policy_id.\
                _compute_value(self)
            self.accrue_expense_journal_id = result

    @api.onchange(
        "accrue_expense_debit_account_policy_id",
    )
    def onchange_accrue_expense_debit_account_id(self):
        self.accrue_expense_debit_account_id = False
        if self.accrue_expense_debit_account_policy_id:
            result = self.accrue_expense_debit_account_policy_id.\
                _compute_value(self)
            self.accrue_expense_debit_account_id = result

    @api.onchange(
        "accrue_expense_credit_account_policy_id",
    )
    def onchange_accrue_expense_credit_account_id(self):
        self.accrue_expense_credit_account_id = False
        if self.accrue_expense_credit_account_policy_id:
            result = self.accrue_expense_credit_account_policy_id.\
                _compute_value(self)
            self.accrue_expense_credit_account_id = result

    @api.onchange(
        "accrue_expense_qty_policy_id",
    )
    def onchange_accrue_expense_qty(self):
        self.accrue_expense_qty = 0.0
        if self.accrue_expense_qty_policy_id:
            result = self.accrue_expense_qty_policy_id.\
                _compute_value(self)
            self.accrue_expense_qty = result

    @api.onchange(
        "accrue_expense_price_policy_id",
    )
    def onchange_accrue_expense_price_unit(self):
        self.accrue_expense_price_unit = 0.0
        if self.accrue_expense_price_policy_id:
            result = self.accrue_expense_price_policy_id.\
                _compute_value(self)
            self.accrue_expense_price_unit = result

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_expense_ok(self):
        self.accrue_expense_ok = self.project_id.accrue_expense_ok

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_expense_journal_policy_id(self):
        self.accrue_expense_journal_policy_id = False
        if self.project_id:
            self.accrue_expense_journal_policy_id = \
                self.project_id.accrue_expense_journal_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_expense_debit_account_policy_id(self):
        self.accrue_expense_debit_account_policy_id = False
        if self.project_id:
            self.accrue_expense_debit_account_policy_id = \
                self.project_id.accrue_expense_debit_account_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_expense_credit_account_policy_id(self):
        self.accrue_expense_credit_account_policy_id = False
        if self.project_id:
            self.accrue_expense_credit_account_policy_id = \
                self.project_id.accrue_expense_credit_account_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_expense_price_policy_id(self):
        self.accrue_expense_price_policy_id = False
        if self.project_id:
            self.accrue_expense_price_policy_id = \
                self.project_id.accrue_expense_price_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_expense_qty_policy_id(self):
        self.accrue_expense_qty_policy_id = False
        if self.project_id:
            self.accrue_expense_qty_policy_id = \
                self.project_id.accrue_expense_qty_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_income_ok(self):
        self.accrue_income_ok = self.project_id.accrue_income_ok

    @api.onchange(
        "accrue_income_journal_policy_id",
    )
    def onchange_accrue_income_journal_id(self):
        self.accrue_income_journal_id = False
        if self.accrue_income_journal_policy_id:
            result = self.accrue_income_journal_policy_id.\
                _compute_value(self)
            self.accrue_income_journal_id = result

    @api.onchange(
        "accrue_income_debit_account_policy_id",
    )
    def onchange_accrue_income_debit_account_id(self):
        self.accrue_income_debit_account_id = False
        if self.accrue_income_debit_account_policy_id:
            result = self.accrue_income_debit_account_policy_id.\
                _compute_value(self)
            self.accrue_income_debit_account_id = result

    @api.onchange(
        "accrue_income_credit_account_policy_id",
    )
    def onchange_accrue_income_credit_account_id(self):
        self.accrue_income_credit_account_id = False
        if self.accrue_income_credit_account_policy_id:
            result = self.accrue_income_credit_account_policy_id.\
                _compute_value(self)
            self.accrue_income_credit_account_id = result

    @api.onchange(
        "accrue_income_qty_policy_id",
    )
    def onchange_accrue_income_qty(self):
        self.accrue_income_qty = 0.0
        if self.accrue_income_qty_policy_id:
            result = self.accrue_income_qty_policy_id.\
                _compute_value(self)
            self.accrue_income_qty = result

    @api.onchange(
        "accrue_income_price_policy_id",
    )
    def onchange_accrue_income_price_unit(self):
        self.accrue_income_price_unit = 0.0
        if self.accrue_income_price_policy_id:
            result = self.accrue_income_price_policy_id.\
                _compute_value(self)
            self.accrue_income_price_unit = result

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_income_journal_policy_id(self):
        self.accrue_income_journal_policy_id = False
        if self.project_id:
            self.accrue_income_journal_policy_id = \
                self.project_id.accrue_income_journal_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_income_debit_account_policy_id(self):
        self.accrue_income_debit_account_policy_id = False
        if self.project_id:
            self.accrue_income_debit_account_policy_id = \
                self.project_id.accrue_income_debit_account_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_income_credit_account_policy_id(self):
        self.accrue_income_credit_account_policy_id = False
        if self.project_id:
            self.accrue_income_credit_account_policy_id = \
                self.project_id.accrue_income_credit_account_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_income_price_policy_id(self):
        self.accrue_income_price_policy_id = False
        if self.project_id:
            self.accrue_income_price_policy_id = \
                self.project_id.accrue_income_price_policy_id

    @api.onchange(
        "project_id",
    )
    def onchange_accrue_income_qty_policy_id(self):
        self.accrue_income_qty_policy_id = False
        if self.project_id:
            self.accrue_income_qty_policy_id = \
                self.project_id.accrue_income_qty_policy_id
