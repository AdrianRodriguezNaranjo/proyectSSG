# -*- coding: utf-8 -*-
# id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
# access_project_manager,proyecto_empresa_contratadora.manager,model_proyecto_empresa_contratadora,proyecto_ssg.group_project_manager,1,1,1,1
# access_project_analyst,proyecto_empresa_contratadora.analyst,model_proyecto_empresa_contratadora,proyecto_ssg.group_project_analyst,1,0,1,0
# access_project_programmer,proyecto_empresa_contratadora.programmer,model_proyecto_empresa_contratadora,proyecto_ssg.group_project_programmer,1,1,0,0

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
    
    proyecto = fields.One2many('project.project','companies', string="Proyecto")

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

     companies = fields.Many2one("proyecto_empresa_contratadora",string="Empresa",required=True,ondelete="cascade")

class proyecto_task(models.Model):
     _name = 'project.task'
     _inherit = 'project.task'
