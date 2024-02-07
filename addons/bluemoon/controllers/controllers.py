# -*- coding: utf-8 -*-
# from odoo import http


# class Bluemoon(http.Controller):
#     @http.route('/bluemoon/bluemoon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bluemoon/bluemoon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bluemoon.listing', {
#             'root': '/bluemoon/bluemoon',
#             'objects': http.request.env['bluemoon.bluemoon'].search([]),
#         })

#     @http.route('/bluemoon/bluemoon/objects/<model("bluemoon.bluemoon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bluemoon.object', {
#             'object': obj
#         })
