# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectoSsg(http.Controller):
#     @http.route('/proyecto_ssg/proyecto_ssg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_ssg/proyecto_ssg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_ssg.listing', {
#             'root': '/proyecto_ssg/proyecto_ssg',
#             'objects': http.request.env['proyecto_ssg.proyecto_ssg'].search([]),
#         })

#     @http.route('/proyecto_ssg/proyecto_ssg/objects/<model("proyecto_ssg.proyecto_ssg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_ssg.object', {
#             'object': obj
#         })
