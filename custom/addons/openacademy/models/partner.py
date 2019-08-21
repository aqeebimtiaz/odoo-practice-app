from datetime import timedelta
from odoo import fields, models, api, exceptions

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("Instructor", default = False)

    session_ids = fields.Many2many('openacademy.session', string = "Attended Sessions", readonly = True)