{
    'name': 'SIMU',
    'version': '1.0.0',
    'summary': 'Module Custom',
    'sequence': 5,
    'description': """
    Simulasi SIMU (Sistem Informasi Manajemen Umat)""",
    'author': 'Dio Antares - 2017730003',
    'company': 'Teknik Informatika UNPAR',
    'website': 'https://dioantares.github.io/',
    'category': 'Customization',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/umat.xml',
        'views/data.xml',
    ],
    'assets': {
        'web.assets_backend': ['Umat/static/src/js/qrcode.js','Umat/static/src/js/qr-scanner.legacy.min.js'],
        'web.assets_common': ['Umat/static/src/js/qr-scanner.legacy.min.js'],
        'web.assets_frontend': ['Umat/static/src/js/qr-scanner.legacy.min.js'],
    },
}