# -*- coding: utf-8 -*-
{
    'name': "My module",

    'summary': """
        Aplicar herencia""",

    'description': """
        Nuevo modulo
    """,

    'author': "AHC",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sales_team','product','sale'],

    # always loaded
    'data': [
       'views/partner_view.xml',
       'views/mymodule_sales_view.xml',
       'views/mymodule_marca_view.xml',
       'views/mymodule_product_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}

