from odoo import models, fields


class ResPartner(models.Model):
    _name = 'aeronix-2'
    _description = 'aeronix employee info'

    name = fields.Many2one("res.partner")
    id_status = fields.Selection([
        ('Passport', "Passport"),
        ('Id', "ID Card"),
        ('driving', "Driving License")
    ])

    id_number= fields.Integer(string='Id number')


