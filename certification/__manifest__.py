{
    'name':'Certification',
    'summary':'Defines certification for different purposes',
    'author':'Eficent, Odoo Community Association (ASO)',
    'website':'https://github.com/neslihanarslan',
    'category':'Certification Management',
    'version':'12.0.1.0.0',
    'license':'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/certification_security.xml',
        'security/ir.model.access.csv',
         'views/certification_view.xml',
         'views/res_partner_view.xml',
         'views/certification_body.xml',
         'views/standard_view.xml',
         'reports/certification_report.xml',
         'reports/certification_template_pdf.xml',
         'reports/report_certification_pdf.xml'


],
    'demo': ['data/certification_data.xml'],
    'development_status': 'Beta',
    'maintainers': ['ceefient'],

}