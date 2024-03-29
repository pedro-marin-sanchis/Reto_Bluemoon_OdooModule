# -*- coding: utf-8 -*-
{
    'name': "Bluemoon",

    'summary': """
        A module to monitor the Bluemoon REST API.""",

    'description': """
        A module to monitor the Bluemoon REST API.
    """,

    'author': "Ugú Informática",
    'website': "https://www.uguinformatica.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Bluemoon',
    'application': True,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'your_module_name/static/lib/Chart.min.js',
        ],
    },
}
