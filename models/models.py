# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyecto_empresa_contratadora(models.Model):
    _name = 'proyecto_empresa_contratadora'
    _description = 'proyecto_empresa_contratadora'

    name = fields.Char('Nombre empresa', required=True)
    empleados = fields.Integer(string="Número de Empleados")
    tipo_empresa = fields.Selection(
        [('microempresa', 'Microempresa'),
         ('pequena_empresa', 'Pequeña empresa'),
         ('mediana_empresa', 'Mediana empresa'),
         ('gran_empresa', 'Gran empresa')],
        string='Tipo de Empresa', compute='_tipoempresa', store=True)
    
    proyecto = fields.Many2one('project.project', string="Proyecto",required=True,ondelete="cascade")

    @api.depends('empleados')
    def _tipoempresa(self):
        for r in self:
            if r.empleados < 10:
                r.tipo_empresa = 'microempresa'
            elif 10 <= r.empleados <= 49:
                r.tipo_empresa = 'pequena_empresa'
            elif 50 <= r.empleados <= 249:
                r.tipo_empresa = 'mediana_empresa'
            else:
                r.tipo_empresa = 'gran_empresa'

class proyecto_proyecto(models.Model):
     _name = 'project.project'
     _inherit = 'project.project'

     companies = fields.One2many("proyecto_empresa_contratadora","proyecto",string="Empresa")