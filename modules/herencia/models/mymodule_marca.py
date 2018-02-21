# -*- coding: utf-8 -*-

from odoo import api,fields,models

class Marca(models.Model):
	_name = 'herencia.marca'

	#crear los campos
	name=fields.Char(string='Marca', required=True)

	codigo = fields.Char(string='Código')

	descripcion=fields.Text(string='Descripción')

	campo = fields.Char(string='Concat',compute='concat')
	
	proveedor_ids = fields.Many2many(
	    'res.partner',
	    string=' '
	)
	producto_ids = fields.One2many(
	    'product.template',
	    'marca_id',
	    string='Productos'
	)

	@api.multi
	@api.depends('name','codigo')
	def concat(self):
		for record in self:
			record.campo = str(record.codigo) +' '+ str(record.name)