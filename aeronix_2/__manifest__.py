{
    'name':'Aeronix-2',
    'summary':'Defines information for Aeronix employee',
    'author':'Neslihan',
    'website':'https://github.com/neslihanarslan',
    'category':'ID Management',
    'version':'12.0.1.0.0',
    'license':'AGPL-3',
    'depends': ['base'],
    'data': [
        'views/aeronix_view.xml',
        'security/ir.model.access.csv'

],
    'development_status': 'Beta',
    'maintainers': ['Tai'],
    'demo': ['data/aeronix_demo.xml'],
}

# entity_mapped = self.env['certification'].search([('entity_id', '=', entity.id)]).mapped('entity_id')
# >>> entity_mapped.name # Test Entity
# >>> test_certificate.unlink() # Unlink certification
# >>> entity.unlink() # Unlink partner
# >>> env.cr.commit() # Commit changes to the database
# >>> quit()

