# -*- coding: utf-8 -*-
{
    'name': "Merced Report",

    'summary': """Informe de Presupuesto""",

    'description': """
        Este informe imprime el nombre del usuario logueado, el cual crea el informe del presupuesto
        """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Sale',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'report/informe_view.xml',
    ],
    'intallable': True,
    'auto_install': False,
}