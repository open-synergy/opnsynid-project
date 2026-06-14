# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectAssignment(models.Model):
    _name = "project.assignment"
    _inherit = [
        "project.assignment",
    ]

    pob_id = fields.Many2one(
        string="# PoB",
        comodel_name="performance_obligation",
        compute="_compute_revenue_recognition_field",
        store=True,
        compute_sudo=True,
    )
    contract_id = fields.Many2one(
        string="# Contract",
        comodel_name="service.contract",
        compute="_compute_revenue_recognition_field",
        store=True,
        compute_sudo=True,
    )

    @api.depends(
        "project_id",
    )
    def _compute_revenue_recognition_field(self):
        PoB = self.env["performance_obligation"]
        Contract = self.env["service.contract"]
        for record in self:
            pob = contract = False
            if record.project_id:
                criteria = [
                    ("project_id", "=", record.project_id.id),
                ]
                pobs = PoB.search(criteria)
                if len(pobs) > 0:
                    pob = pobs[0]
                    # Performance obligation is no longer linked to a service
                    # contract directly. Resolve the originating contract through
                    # the shared analytic account instead.
                    if pob.source_analytic_account_id:
                        contract = Contract.search(
                            [
                                (
                                    "analytic_account_id",
                                    "=",
                                    pob.source_analytic_account_id.id,
                                )
                            ],
                            limit=1,
                        )
            record.pob_id = pob
            record.contract_id = contract
