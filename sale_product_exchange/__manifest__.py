# -*- coding: utf-8 -*-
{
    'name': "Sale Product Exchange",

    'summary': 'Sales Exchange process',

    'description': """
        Sales Exchange Products
          This module allows to exchange products form delivery order
          Also allows to add new products during the exchange process
          exchanged products and new added products added in the same Sales Order
          
    """,

    'author': "Keroles Ayed",
    'website': "https://www.linkedin.com/in/keroles-ayed-19788b14a/",
    'version': '15',
    'license': 'LGPL-3',

    'depends': ['stock'],

    'data': [
        'security/ir.model.access.csv',
        'views/exchange_view.xml',
    ],
}
