from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'hr.employee'

    id_status = fields.Selection([
        ('Passport', "Passport"),
        ('Id', "ID Card"),
        ('driving', "Driving License")
    ])

    id_number= fields.Integer(string='Id number')

