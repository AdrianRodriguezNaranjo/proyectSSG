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
     _inherit = 'project.project'

     companies = fields.Many2one("proyecto_empresa_contratadora",string="Empresa")
     tasks = fields.One2many('project.task','projects_id', string="Tareas")

class proyecto_task(models.Model):
     _inherit = 'project.task'

     projects = fields.Many2one("project.project",string="Proyectos")
