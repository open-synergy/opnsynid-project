# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import _, fields, models
from odoo.exceptions import UserError

from odoo.addons.ssi_decorator import ssi_decorator


class ResponSibleTaskMixin(models.AbstractModel):
    _name = "mixin.responsible_task"
    _inherit = [
        "mixin.decorator",
    ]
    _description = "Responsible Task Mixin"
    _responsible_task_create_page = True
    _responsible_task_page_xpath = "//page[last()]"

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        ondelete="restrict",
    )
    responsible_default_stage_id = fields.Many2one(
        string="Default Responsible Task Stage",
        comodel_name="project.task.type",
        ondelete="restrict",
    )
    responsible_default_type_id = fields.Many2one(
        string="Default Responsible Task Type",
        comodel_name="task.type",
        ondelete="restrict",
    )
    responsible_task_id = fields.Many2one(
        string="Responsible Task",
        comodel_name="project.task",
        ondelete="restrict",
    )
    responsible_stage_id = fields.Many2one(
        string="Responsible Task Stage",
        related="responsible_task_id.stage_id",
        store=True,
        compute_sudo=True,
    )
    responsible_state = fields.Selection(
        string="Responsible Task State",
        related="responsible_task_id.state",
        store=True,
        compute_sudo=True,
    )

    def action_create_responsible_task(self):
        for record in self.sudo():
            record._create_responsible_task()

    def action_delete_responsible_task(self):
        for record in self.sudo():
            record._delete_responsible_task()

    def _delete_responsible_task(self):
        self.ensure_one()
        if not self.responsible_task_id:
            return True

        task = self.responsible_task_id

        self.write(
            {
                "responsible_task_id": False,
            }
        )

        task.unlink()

    @ssi_decorator.insert_on_form_view()
    def _responsible_task_insert_form_element(self, view_arch):
        if self._responsible_task_create_page:
            view_arch = self._add_view_element(
                view_arch=view_arch,
                qweb_template_xml_id="ssi_task_mixin.responsible_task_form",
                xpath=self._responsible_task_page_xpath,
                position="after",
            )
        return view_arch

    def _create_responsible_task(self):
        self.ensure_one()
        task = self.env["project.task"].create(
            self._prepare_create_responsible_task(),
        )
        self.write(
            {
                "responsible_task_id": task.id,
            }
        )

    def _prepare_create_responsible_task(self):
        self.ensure_one()
        project = self._get_project_id()
        stage = self._get_responsible_default_stage_id()
        task_type = self._get_responsible_default_type_id()
        return {
            "name": self.name,
            "project_id": project.id,
            "stage_id": stage.id,
            "type_id": task_type.id,
            "user_id": self.user_id.id,
        }

    def _get_responsible_default_stage_id(self):
        self.ensure_one()
        result = self.responsible_default_stage_id

        if not result:
            error_message = _(
                """
            Context: Create responsible task from %s
            Database ID: %s
            Problem: No Default Responsible Task Stage selected
            Solution: Select Default Responsible Task Stage on Project tab
            """
                % (self._description, self.id)
            )
            raise UserError(error_message)
        return result

    def _get_responsible_default_type_id(self):
        self.ensure_one()
        result = self.responsible_default_type_id

        if not result:
            error_message = _(
                """
            Context: Create responsible task from %s
            Database ID: %s
            Problem: No Default Responsible Task Type selected
            Solution: Select Default Responsible Task Type on Project tab
            """
                % (self._description, self.id)
            )
            raise UserError(error_message)
        return result

    def _get_project_id(self):
        self.ensure_one()
        result = self.project_id

        if not result:
            error_message = _(
                """
            Context: Create responsible task from %s
            Database ID: %s
            Problem: No project selected
            Solution: Select Project on Project tab
            """
                % (self._description, self.id)
            )
            raise UserError(error_message)
        return result
