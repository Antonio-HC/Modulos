# -*- coding: utf-8 -*-

from odoo import fields,models

class sales(models.Model):

	_inherit = 'res.partner'

	fecha_cobro = fields.Date(String='Fecha de cobro')
