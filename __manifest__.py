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
        'base',
        'mail',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu.xml',
        'views/feedback_input_view.xml',
        'report/employee_report.xml',
        'report/report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ecg_appraisals_app/static/src/css/ecg.css'
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}