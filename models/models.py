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
    
    # proyectos_contratados = fields.One2many('proyecto.proyecto', 'empresa_contratadora_id', string='Proyectos Contratados')

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
