# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import _, api, models
from openerp.exceptions import Warning as UserError


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    def write(self, vals):
        for record in self:
            if "stage_id" in vals:
                if not record._check_allowed_stage_no_restrict():
                    if not record._check_allowed_stage(vals):
                        stage_name = self._get_stage_name(vals.get("stage_id"))
                        raise UserError(
                            _(
                                "Stage %s is not allowed "
                                "to be changed to stage %s."
                                % (record.stage_id.name, stage_name)
                            )
                        )
        return super(ProjectTask, self).write(vals)

    @api.multi
    def _get_stage_name(self, stage_id):
        result = ""
        obj_project_task_type = self.env["project.task.type"]
        if stage_id:
            result = obj_project_task_type.browse(stage_id).name
        return result

    @api.multi
    def _check_allowed_stage(self, vals):
        self.ensure_one()
        allowed_stage_ids = self.stage_id.allowed_stage_ids
        if allowed_stage_ids:
            if vals.get("stage_id") in allowed_stage_ids.ids:
                return True
            else:
                return False
        return True

    @api.multi
    def _check_allowed_stage_no_restrict(self):
        self.ensure_one()
        no_restrict_ok = self.project_id.no_restrict_ok
        return no_restrict_ok
