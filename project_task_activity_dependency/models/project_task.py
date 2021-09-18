# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ProjectTask(models.Model):
    _inherit = "project.task"

    predecessor_ids = fields.One2many(
        string="Predecessor",
        comodel_name="project.task_dependency",
        inverse_name="task_id",
    )
    sucessor_ids = fields.One2many(
        string="Sucessor",
        comodel_name="project.task_dependency",
        inverse_name="predecessor_task_id",
    )

    @api.constrains(
        "state",
    )
    def check_dependency(self):
        if self.state == "open":
            if not self._check_dependency("start_start"):
                msg = _(
                    "Please start/finish/cancel all predecessors with "
                    "start-to-start dependency"
                )
                raise UserError(msg)
            if not self._check_dependency("finish_start"):
                msg = _(
                    "Please finish/cancel all predecessors with "
                    "finish-to-start dependency"
                )
                raise UserError(msg)
        elif self.state == "done":
            if not self._check_dependency("start_finish"):
                msg = _(
                    "Please start/finish/cancel all predecessors with "
                    "start-to-finish dependency"
                )
                raise UserError(msg)
            if not self._check_dependency("finish_finish"):
                msg = _(
                    "Please finish/cancel all predecessors with "
                    "finish-to-finish dependency"
                )
                raise UserError(msg)

    @api.multi
    def _check_dependency(self, dependency_type):
        obj_task = self.env["project.task_dependency"]
        if dependency_type == "start_start":
            domain = self._prepare_start_to_start_domain()
        elif dependency_type == "finish_start":
            domain = self._prepare_finish_to_start_domain()
        elif dependency_type == "start_finish":
            domain = self._prepare_start_to_finish_domain()
        elif dependency_type == "finish_finish":
            domain = self._prepare_finish_to_finish_domain()
        task_count = obj_task.search_count(domain)
        if task_count > 0:
            return False
        else:
            return True

    @api.multi
    def _prepare_start_to_start_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "start_start"),
            ("predecessor_task_id.state", "not in", ["open", "cancelled", "done"]),
        ]

    @api.multi
    def _prepare_finish_to_start_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "finish_start"),
            ("predecessor_task_id.state", "not in", ["cancelled", "done"]),
        ]

    @api.multi
    def _prepare_start_to_finish_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "start_finish"),
            ("predecessor_task_id.state", "not in", ["open", "cancelled", "done"]),
        ]

    @api.multi
    def _prepare_finish_to_finish_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "finish_finish"),
            ("predecessor_task_id.state", "not in", ["cancelled", "done"]),
        ]
