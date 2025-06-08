# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    milestone_id = fields.Many2one(
        string="Milestone",
        comodel_name="project_milestone",
        ondelete="restrict",
    )
    phase_id = fields.Many2one(
        string="Phase",
        comodel_name="project_phase",
        ondelete="restrict",
    )
    deliverable_id = fields.Many2one(
        string="Deliverable",
        comodel_name="project_deliverable",
        ondelete="restrict",
    )
    specification = fields.Text(
        string="Specification",
    )
    instruction_ids = fields.One2many(
        string="Task Instructions",
        comodel_name="task.instruction",
        inverse_name="task_id",
    )
    predecessor_ids = fields.One2many(
        string="Predecessor",
        comodel_name="task.dependency",
        inverse_name="task_id",
    )
    sucessor_ids = fields.One2many(
        string="Sucessor",
        comodel_name="task.dependency",
        inverse_name="predecessor_task_id",
    )
    dependency_state = fields.Selection(
        string="Dependency Status",
        selection=[
            ("normal", "In Progress"),
            ("done", "Ready"),
            ("blocked", "Blocked"),
        ],
        compute="_compute_dependency_state",
        store=True,
    )

    @api.onchange(
        "project_id",
    )
    def onchange_milestone_id(self):
        self.milestone_id = False

    @api.depends(
        "stage_id",
        "predecessor_ids",
        "predecessor_ids.predecessor_task_id",
        "predecessor_ids.predecessor_task_id.stage_id",
    )
    def _compute_dependency_state(self):
        TaskDependency = self.env["task.dependency"]
        for record in self:
            result = "normal"
            if record.predecessor_ids:
                # print("\n record.state", record.state)
                if record.state == "draft":
                    criteria = [
                        ("task_id", "=", record.id),
                        ("dependency_type", "=", "start_start"),
                    ]
                    count_all = TaskDependency.search_count(criteria)
                    criteria += [
                        ("predecessor_task_state", "in", ["open", "done", "cancelled"]),
                    ]
                    count_ok = TaskDependency.search_count(criteria)
                    if count_all == count_ok:
                        result = "done"
                    else:
                        result = "blocked"
                    # kalau sudah blocked tidak perlu dilanjutkan
                    if result == "done":
                        criteria = [
                            ("task_id", "=", record.id),
                            ("dependency_type", "=", "finish_start"),
                        ]
                        count_all = TaskDependency.search_count(criteria)
                        criteria += [
                            ("predecessor_task_state", "in", ["done", "cancelled"]),
                        ]
                        count_ok = TaskDependency.search_count(criteria)
                        if count_all == count_ok:
                            result = "done"
                        else:
                            result = "blocked"
                elif record.state == "open":
                    criteria = [
                        ("task_id", "=", record.id),
                        ("dependency_type", "=", "start_finish"),
                    ]
                    count_all = TaskDependency.search_count(criteria)
                    criteria += [
                        ("predecessor_task_state", "in", ["open", "done", "cancelled"]),
                    ]
                    count_ok = TaskDependency.search_count(criteria)
                    if count_all == count_ok:
                        result = "done"
                    else:
                        result = "blocked"
                    # kalau sudah blocked tidak perlu dilanjutkan
                    if result == "done":
                        criteria = [
                            ("task_id", "=", record.id),
                            ("dependency_type", "=", "finish_finish"),
                        ]
                        count_all = TaskDependency.search_count(criteria)
                        criteria += [
                            ("predecessor_task_state", "in", ["done", "cancelled"]),
                        ]
                        count_ok = TaskDependency.search_count(criteria)
                        if count_all == count_ok:
                            result = "done"
                        else:
                            result = "blocked"

            record.dependency_state = result

    @api.constrains(
        "state",
    )
    def check_dependency(self):
        for record in self:
            if record.state == "open":
                if not record._check_dependency("start_start"):
                    msg = _(
                        "Please start/finish/cancel all predecessors with "
                        "start-to-start dependency"
                    )
                    raise ValidationError(msg)
                if not record._check_dependency("finish_start"):
                    msg = _(
                        "Please finish/cancel all predecessors with "
                        "finish-to-start dependency"
                    )
                    raise ValidationError(msg)
            elif record.state == "done":
                if not record._check_dependency("start_finish"):
                    msg = _(
                        "Please start/finish/cancel all predecessors with "
                        "start-to-finish dependency"
                    )
                    raise ValidationError(msg)
                if not record._check_dependency("finish_finish"):
                    msg = _(
                        "Please finish/cancel all predecessors with "
                        "finish-to-finish dependency"
                    )
                    raise ValidationError(msg)

    def _check_dependency(self, dependency_type):
        self.ensure_one()
        TaskDependency = self.env["task.dependency"]
        if dependency_type == "start_start":
            domain = self._prepare_start_to_start_domain()
        elif dependency_type == "finish_start":
            domain = self._prepare_finish_to_start_domain()
        elif dependency_type == "start_finish":
            domain = self._prepare_start_to_finish_domain()
        else:  # finish_finish
            domain = self._prepare_finish_to_finish_domain()
        task_count = TaskDependency.search_count(domain)
        if task_count > 0:
            return False
        else:
            return True

    def _prepare_start_to_start_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "start_start"),
            ("predecessor_task_id.state", "not in", ["open", "cancelled", "done"]),
        ]

    def _prepare_finish_to_start_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "finish_start"),
            ("predecessor_task_id.state", "not in", ["cancelled", "done"]),
        ]

    def _prepare_start_to_finish_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "start_finish"),
            ("predecessor_task_id.state", "not in", ["open", "cancelled", "done"]),
        ]

    def _prepare_finish_to_finish_domain(self):
        self.ensure_one()
        return [
            ("task_id", "=", self.id),
            ("dependency_type", "=", "finish_finish"),
            ("predecessor_task_id.state", "not in", ["cancelled", "done"]),
        ]
