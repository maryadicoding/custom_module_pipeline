# -*- coding: utf-8 -*-

{
    'name': 'SmartERP Contact Report Pipeline',
    'version': '2.0',
    'category': 'report group BY',
    'summary': 'Modification of customer and report pieline module',
    'author': 'Maryadi',
    'email': 'maryadi@proxsisgroup.com',
    'website': 'http://www.proxsisgroup.com',
    'maintainer': 'BizTech Proxsis IT',
    'license': 'AGPL-3',
    'depends': ['event','base','contacts'],
    'data': [
        'views/customer_view.xml',
        #'views/search.xml',
    ],
    'images': ['static/description/smarterp.png'],
    'installable': True,
    'auto_install': False
}