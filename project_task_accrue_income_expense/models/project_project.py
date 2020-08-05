# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

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
    accrue_income_journal_policy_id = fields.Many2one(
        string="Accrue Income Journal Policy",
        comodel_name="project.task_accrue_journal_policy",
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
