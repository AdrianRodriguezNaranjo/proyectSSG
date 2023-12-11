# -*- coding: utf-8 -*-
{
    'name': "proyectoSSG",

    'summary': """
        Modelo para empresas contratadoras """,

    'description': """
        Proyecto de integración temprana SSG
    """,

    'author': "Adrián Rodríguez Naranjo",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/proyecto_ssg_reglas_registro.xml',
        'data/proyecto_etapa_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application':'True',

    # assets
    'assets':{
        'web.assets_common': [
            'proyecto_ssg/static/src/scss/style1.scss',
        ]
    }
}
