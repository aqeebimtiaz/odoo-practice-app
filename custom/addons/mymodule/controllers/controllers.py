# -*- coding: utf-8 -*-
from odoo import http

# class Mymodule(http.Controller):
#     @http.route('/mymodule/mymodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mymodule/mymodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mymodule.listing', {
#             'root': '/mymodule/mymodule',
#             'objects': http.request.env['mymodule.mymodule'].search([]),
#         })

#     @http.route('/mymodule/mymodule/objects/<model("mymodule.mymodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mymodule.object', {
#             'object': obj
#         })