# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class BatchProjectAssignment(models.Model):
    _name = "project.batch_assignment"
    _inherit = [
        "project.batch_assignment",
    ]

    pob_id = fields.Many2one(
        string="# PoB",
        comodel_name="service_contract.performance_obligation",
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
        PoB = self.env["service_contract.performance_obligation"]
        for record in self:
            pob = contract = False
            if record.project_id:
                criteria = [
                    ("project_id", "=", record.project_id.id),
                ]
                pobs = PoB.search(criteria)
                if len(pobs) > 0:
                    pob = pobs[0]
                    contract = pob.contract_id
            record.pob_id = pob
            record.contract_id = contract
