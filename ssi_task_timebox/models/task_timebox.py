# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class TaskTimebox(models.Model):
    _name = "task.timebox"
    _inherit = [
        "mixin.master_data",
        "mixin.date_duration",
    ]
    _description = "Task Timebox"
    _order = "date_start, id"

    task_ids = fields.Many2many(
        string="Timeboxes",
        comodel_name="project.task",
        relation="rel_timebox_2_task",
        column1="timebox_id",
        column2="task_id",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("open", "On Progress"),
            ("done", "Done"),
        ],
        default="new",
    )

    def action_open(self):
        for document in self:
            document.write(document._prepare_open_data())
            document._set_on_running_timebox()

    def _prepare_open_data(self):
        self.ensure_one()
        return {
            "state": "open",
        }

    def _set_on_running_timebox(self):
        self.ensure_one()
        self.task_ids.write({"on_running_timebox": True})

    def _set_off_running_timebox(self):
        self.ensure_one()
        self.task_ids.write({"on_running_timebox": False})

    def action_done(self):
        for document in self:
            document.write(document._prepare_done_data())
            document._set_off_running_timebox()

    def _prepare_done_data(self):
        self.ensure_one()
        return {
            "state": "done",
        }

    def action_restart(self):
        for document in self:
            document.write(document._prepare_restart_data())
            document._set_off_running_timebox()

    def _prepare_restart_data(self):
        self.ensure_one()
        return {
            "state": "new",
        }

    @api.constrains(
        "state",
    )
    def _check_open_timebox(self):
        strWarning = _("Only 1 timebox can be opened")
        obj_timebox = self.env["task.timebox"]
        for document in self:
            if document.state == "open":
                check_timebox = obj_timebox.search(
                    [("state", "=", "open"), ("id", "!=", document.id)]
                )
                if len(check_timebox) > 0:
                    raise UserError(strWarning)

    def find_next(self):
        self.ensure_one()
        result = False
        criteria = [("date_start", ">", self.date_start), ("id", "!=", self.id)]
        timeboxes = self.search(criteria)
        if len(timeboxes) > 0:
            result = timeboxes[0]
        return result

    def find_previous(self):
        self.ensure_one()
        result = False
        criteria = [("date_start", "<", self.date_start), ("id", "!=", self.id)]
        timeboxes = self.search(criteria)
        if len(timeboxes) > 0:
            result = timeboxes[0]
        return result
