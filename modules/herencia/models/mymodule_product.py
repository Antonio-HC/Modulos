# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Product(models.Model):
	_inherit = 'product.template'

	#crear relacion
	marca_id=fields.Many2one(
	    'herencia.marca',
	    string='Marca',
	    ondelete='cascade'
	)
	generico = fields.Boolean(
	    string='Genérico',
	)

	impuesto_p = fields.Float(string='Porcentaje impuesto',default=1)
	impuesto = fields.Float(string='Impuesto')

	@api.multi
	@api.onchange('impuesto_p','list_price')
	def _calc_impuesto(self):
		if self.impuesto_p <= 0:
			return {
			'warning': {
				'title': ("El impuesto debe ser mayor a 0"),
				'message': ("Seleccione un numero mayor"),
				},
			}
		if self.impuesto_p > 0:
			self.impuesto = (self.impuesto_p * self.list_price)/100
