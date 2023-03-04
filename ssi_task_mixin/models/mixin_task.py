# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from lxml import etree

from odoo import api, fields, models


class MixinTask(models.AbstractModel):
    _name = "mixin.task"
    _description = "Mixin for Object Tasks"

    _task_create_page = False
    _task_page_xpath = "//page[1]"
    _task_template_position = "before"

    need_task = fields.Boolean(
        string="Need Task",
        default=False,
    )
    task_ids = fields.Many2many(
        string="Tasks",
        comodel_name="project.task",
        copy=False,
    )
    total_task = fields.Integer(
        string="Total Task",
        compute="_compute_task",
        store=True,
    )
    task_draft_count = fields.Integer(
        string="Task Draft Count",
        compute="_compute_task",
        store=True,
    )
    task_open_count = fields.Integer(
        string="Task Open Count",
        compute="_compute_task",
        store=True,
    )
    task_done_count = fields.Integer(
        string="Task Done Count",
        compute="_compute_task",
        store=True,
    )
    task_pending_count = fields.Integer(
        string="Task Pending Count",
        compute="_compute_task",
        store=True,
    )
    task_no_state_count = fields.Integer(
        string="Task No State Count",
        compute="_compute_task",
        store=True,
    )
    task_done = fields.Boolean(
        string="Task Done",
        compute="_compute_task",
        store=True,
    )
    timebox_latest_id = fields.Many2one(
        string="Letest Timebox",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_latest_date_start = fields.Date(
        string="Latest Timebox Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_latest_date_end = fields.Date(
        string="Lates Timebox Date End",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_id = fields.Many2one(
        string="Timebox Initial",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_start = fields.Date(
        string="Timebox Initial Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_end = fields.Date(
        string="Timebox Initial Date End",
        compute="_compute_timebox",
        store=True,
    )

    @api.depends(
        "task_ids",
        "task_ids.stage_id",
        "task_ids.state",
    )
    def _compute_task(self):
        for record in self:
            total_task = (
                task_no_state_count
            ) = (
                task_draft_count
            ) = task_open_count = task_done_count = task_pending_count = 0
            task_done = False
            if record.task_ids:
                for task in record.task_ids:
                    total_task += 1
                    if task.state == "draft":
                        task_draft_count += 1
                    elif task.state == "open":
                        task_open_count += 1
                    elif task.state == "done":
                        task_done_count += 1
                    elif task.state == "pending":
                        task_pending_count += 1
                    else:
                        task_no_state_count += 1
                if total_task == task_done_count:
                    task_done = True
            record.total_task = total_task
            record.task_draft_count = task_draft_count
            record.task_open_count = task_open_count
            record.task_done_count = task_done_count
            record.task_no_state_count = task_no_state_count
            record.task_pending_count = task_pending_count
            record.task_done = task_done

    @api.depends(
        "task_ids",
        "task_ids.timebox_latest_id",
        "task_ids.timebox_date_start",
        "task_ids.timebox_date_end",
        "task_ids.timebox_initial_id",
        "task_ids.timebox_initial_date_start",
        "task_ids.timebox_initial_date_end",
        "task_ids.timebox_upcoming_id",
        "task_ids.timebox_upcoming_date_start",
        "task_ids.timebox_upcoming_date_end",
    )
    def _compute_timebox(self):
        for document in self:
            timebox_latest_id = (
                timebox_latest_date_start
            ) = (
                timebox_latest_date_end
            ) = (
                timebox_initial_id
            ) = timebox_initial_date_start = timebox_initial_date_end = False

            if document.task_ids:
                tasks = document.task_ids
                latest_sorted = tasks.sorted(key=lambda r: r.timebox_latest_id)
                timebox_latest_id = latest_sorted[0].timebox_latest_id
                timebox_latest_date_start = timebox_latest_id.date_start
                timebox_latest_date_end = timebox_latest_id.date_end
                initial_sorted = tasks.sorted(key=lambda r: r.timebox_initial_id)
                timebox_initial_id = initial_sorted[-1].timebox_initial_id
                timebox_initial_date_start = timebox_initial_id.date_start
                timebox_initial_date_end = timebox_initial_id.date_end

            document.timebox_latest_id = timebox_latest_id
            document.timebox_latest_date_start = timebox_latest_date_start
            document.timebox_latest_date_end = timebox_latest_date_end
            document.timebox_initial_id = timebox_initial_id
            document.timebox_initial_date_start = timebox_initial_date_start
            document.timebox_initial_date_end = timebox_initial_date_end

    def action_open_task(self):
        for record in self.sudo():
            result = record._open_task()
        return result

    def _open_task(self):
        waction = self.env.ref("project.action_view_all_task").read()[0]
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("id", "in", self.task_ids.ids)],
                "context": {},
            }
        )
        return waction

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        res = super().fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        if view_type == "form" and self._task_create_page:
            doc = etree.XML(res["arch"])
            node_xpath = doc.xpath(self._task_page_xpath)
            if node_xpath:
                str_element = self.env["ir.qweb"]._render(
                    "ssi_task_mixin.task_mixin_template"
                )
                for node in node_xpath:
                    new_node = etree.fromstring(str_element)
                    if self._task_template_position == "after":
                        node.addnext(new_node)
                    elif self._task_template_position == "before":
                        node.addprevious(new_node)

            View = self.env["ir.ui.view"]

            if view_id and res.get("base_model", self._name) != self._name:
                View = View.with_context(base_model_name=res["base_model"])
            new_arch, new_fields = View.postprocess_and_fields(doc, self._name)
            res["arch"] = new_arch
            new_fields.update(res["fields"])
            res["fields"] = new_fields
        return res
