# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyecto_ssg(models.Model):
#     _name = 'proyecto_ssg.proyecto_ssg'
#     _description = 'proyecto_ssg.proyecto_ssg'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
# models.py

from odoo import models, fields, api

class empresa_contratadora(models.Model):
    _name = 'proyecto.empresa_contratadora'
    _description = 'proyecto.empresa_contratadora'

    name = fields.Char('Nombre empresa', required=True)
    empleados = fields.Char(string="Empleados")

    # proyectos_ids = fields.One2many('proyecto.proyecto', 'empresa_contratadora_id', 'Proyectos Contratados')

# class Proyecto(models.Model):
#     _name = 'proyecto.proyecto'
#     _description = 'Proyectos'

#     name = fields.Char('Nombre', required=True)
#     empresa_contratadora_id = fields.Many2one('proyecto.empresa_contratadora', 'Empresa Contratadora')
#     tareas_ids = fields.One2many('proyecto.tarea', 'proyecto_id', 'Tareas')

# class Tarea(models.Model):
#     _name = 'proyecto.tarea'
#     _description = 'Tareas'

#     name = fields.Char('Nombre', required=True)
#     proyecto_id = fields.Many2one('proyecto.proyecto', 'Proyecto')
#     analista_id = fields.Many2one('res.users', 'Analista')
#     subtareas_ids = fields.One2many('proyecto.subtarea', 'tarea_id', 'Subtareas')

# class Subtarea(models.Model):
#     _name = 'proyecto.subtarea'
#     _description = 'Subtareas'

#     name = fields.Char('Nombre', required=True)
#     tarea_id = fields.Many2one('proyecto.tarea', 'Tarea')

