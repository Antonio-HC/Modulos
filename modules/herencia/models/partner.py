# -*- coding: utf-8 -*-

from odoo import api,fields, models

class Partner(models.Model):

    _inherit = 'res.partner'
    # Herencia Odoo
    
    edad = fields.Char(String='Edad')

