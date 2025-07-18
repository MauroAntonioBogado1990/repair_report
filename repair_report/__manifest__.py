{
    'name': 'Repair Report',
    'version': '15.0',
    'category': 'Tools',
    'author':'Mauro Bogado',
    'summary': 'Modulo para poder realizar reporte de reparaciones',
    'depends': ['base','repair'],
    'data': [
        #'security/ir.model.access.csv',
        'views/repair_report.xml',
        'report/repair_reporte.xml',
    ],
    'installable': True,
    'application': False,
}   