# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    @api.depends(
        "qc_question_ids", "qc_question_ids.success",
    )
    def _compute_qc_result(self):
        for report in self:
            result = True
            if report.qc_question_ids:
                qc = report.qc_question_ids.filtered(lambda r: not r.success)
                if len(qc) > 0:
                    result = False
            report.qc_pass = result

    qc_pass = fields.Boolean(
        string="QC Passed?",
        compute="_compute_qc_result",
        store=True,
    )
    qc_question_ids = fields.One2many(
        string="Questions",
        comodel_name="project.task_qc_question",
        inverse_name="task_id",
        copy=False,
        readonly=True,
        states={
            "open": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        _super = super(ProjectTask, self)
        result = _super._prepare_confirm_data()
        result.update({
            "qc_question_ids": self.categ_id._prepare_qc_question()
        })
        return result

    @api.constrains(
        "qc_pass", "state"
    )
    def _check_qc_pass(self):
        if self.state == "done" and not self.qc_pass:
            warning_msg = _("Report does not pass qc check")
            raise UserError(warning_msg)
