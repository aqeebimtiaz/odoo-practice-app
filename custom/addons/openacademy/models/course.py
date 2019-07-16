# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string = "Title", required = True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', ondelete = 'set null', string = "Responsible", index = True)

    session_ids = fields.One2many('openacademy.session', 'course_id', string = "Sessions")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))]
        )
        if not copied_count:
            new_name = u"Copy of {}%".format(self.name)
        else:
            new_name = u"Copy of {}%".format(self.name, copied_count)
        
        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)', "Course title should not be equal to description."),
        ('name_unique', 'UNIQUE(name)', "Course title must be unique.")
    ]