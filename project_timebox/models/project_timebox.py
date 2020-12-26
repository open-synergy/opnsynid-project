# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class ProjectTimebox(models.Model):
    _name = "project.timebox"
    _descrption = "Project Timebox"
    _order = "date_start, id"

    name = fields.Char(
        string="Timebox",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_stop = fields.Date(
        string="Date Stop",
        required=True,
    )
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

    @api.multi
    def action_open(self):
        for document in self:
            document.write(document._prepare_open_data())
            document._set_on_running_timebox()

    @api.multi
    def _prepare_open_data(self):
        self.ensure_one()
        return {
            "state": "open",
        }

    @api.multi
    def _set_on_running_timebox(self):
        self.ensure_one()
        self.task_ids.write({"on_running_timebox": True})

    @api.multi
    def _set_off_running_timebox(self):
        self.ensure_one()
        self.task_ids.write({"on_running_timebox": False})

    @api.multi
    def action_done(self):
        for document in self:
            document.write(document._prepare_done_data())
            document._set_off_running_timebox()

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        return {
            "state": "done",
        }

    @api.multi
    def action_restart(self):
        for document in self:
            document.write(document._prepare_restart_data())
            document._set_off_running_timebox()

    @api.multi
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
        obj_timebox = self.env["project.timebox"]
        for document in self:
            if document.state == "open":
                check_timebox = obj_timebox.search(
                    [("state", "=", "open"), ("id", "!=", document.id)]
                )
                if len(check_timebox) > 0:
                    raise UserError(strWarning)
