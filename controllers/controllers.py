# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo502(http.Controller):
#     @http.route('/odoo502/odoo502/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo502/odoo502/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo502.listing', {
#             'root': '/odoo502/odoo502',
#             'objects': http.request.env['odoo502.odoo502'].search([]),
#         })

#     @http.route('/odoo502/odoo502/objects/<model("odoo502.odoo502"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo502.object', {
#             'object': obj
#         })
