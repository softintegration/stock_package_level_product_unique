# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class StockPackageLevel(models.Model):
    _inherit = 'stock.package_level'

    global_quantity = fields.Float(string='Global quantity',related='package_id.global_quantity',store=True)

    

