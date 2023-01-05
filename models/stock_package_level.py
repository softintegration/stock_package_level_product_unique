# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class StockPackageLevel(models.Model):
    _inherit = 'stock.package_level'

    global_quantity = fields.Float(string='Global quantity',related='package_id.global_quantity',store=True)
    product_id = fields.Many2one('product.product', string='Product', related='package_id.product_id', store=True)
    

