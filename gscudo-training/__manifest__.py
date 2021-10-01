# -*- coding: utf-8 -*-
{
    'name': "Gruppo Scudo Formazione",

    'summary': """
      Gruppo Scudo Trainig courses customizations
        """,

    'description': """
      This module adds customizations to manage Trainig Courses
        
    """,

    'author': "Gruppo Scudo Srl / LGIT",
    'website': "http://www.grupposcudo.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'GruppoScudo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'contacts',
                'project',
                'gscudo-sg'
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_groups.xml',
        'views/menus.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/planner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# 13.08
# 16 
# marche