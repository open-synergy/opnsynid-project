# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _inherit = 'project.project'

    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'New'),
            ('open', 'In Progress'),
            ('done', 'Done'),
            ('pending', 'Pending'),
            ('cancel', 'Cancel'),
        ], default='draft', copy=False)

    def action_confirm(self):
        for rec in self.filtered(lambda p: p.state == 'draft'):
            rec.write({
                'state': 'open',
            })

    def action_done(self):
        for rec in self.filtered(lambda p: p.state == 'open'):
            rec.write({
                'state': 'done',
            })

    def action_pending(self):
        for rec in self.filtered(lambda p: p.state == 'open'):
            rec.write({
                'state': 'pending',
            })

    def action_cancel(self):
        for rec in self.filtered(lambda p: p.state in ['draft', 'open', 'pending', 'done']):
            rec.write({
                'state': 'cancel',
            })

    def action_draft(self):
        for rec in self.filtered(lambda p: p.state == 'cancel'):
            rec.write({
                'state': 'draft',
            })
