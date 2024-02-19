from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.model
    def default_get(self, fields):
        res = super(MailComposeMessage, self).default_get(fields=fields)
        if self.env.context.get('default_model') == 'project.task':
            res['partner_ids'] = False
        return res
