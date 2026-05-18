from odoo import models, fields

class CustomModelA(models.Model):
    _name = 'custom.model.a'
    _description = 'Custom Model A'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence')
    sel = fields.Selection([("s", "Small"), ("l", "Large")])

    _name_sel_uniq = models.Constraint('UNIQUE(name, sel)',"Data unique")


class CustomModelB(models.Model):
    _name = 'custom.model.b'
    _description = 'Custom Model B'

    label = fields.Char()
    model_a_id = fields.Many2one("custom.model.a")
