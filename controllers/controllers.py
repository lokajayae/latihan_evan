# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanEvan(http.Controller):
#     @http.route('/latihan_evan/latihan_evan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_evan/latihan_evan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_evan.listing', {
#             'root': '/latihan_evan/latihan_evan',
#             'objects': http.request.env['latihan_evan.latihan_evan'].search([]),
#         })

#     @http.route('/latihan_evan/latihan_evan/objects/<model("latihan_evan.latihan_evan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_evan.object', {
#             'object': obj
#         })
