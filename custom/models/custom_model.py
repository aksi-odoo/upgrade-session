from odoo import models, fields

class CustomModelA(models.Model):
    _name = 'custom.model.a'
    _description = 'Custom Model A'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence')
    sel = fields.Selection([("s", "S"), ("m", "M"), ("l", "L")])

    _sql_constraints = [("data_uniq", "UNIQUE(name, sel)", "Data unique")]


class CustomModelB(models.Model):
    _name = 'custom.model.b'
    _description = 'Custom Model B'

    name = fields.Char()
    modela_id = fields.Many2one("custom.model.a")
