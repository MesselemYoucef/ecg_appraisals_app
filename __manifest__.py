# -*- coding: utf-8 -*-
{
    'name': 'ECG Appraisals',
    'version': '1.0',
    'summary': 'Emirates Consulting Group Appraisals',
    'sequence': -103,
    'description': """Emirates Consulting Group Appraisals""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/feedback_input_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}