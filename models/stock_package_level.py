# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class StockPackageLevel(models.Model):
    _inherit = 'stock.package_level'

    global_quantity = fields.Float(string='Qty to do',related='package_id.global_quantity',digits='Product Unit of Measure',store=True)
    qty_done = fields.Float(string='Done',digits='Product Unit of Measure',compute='_compute_qty_done')
    product_id = fields.Many2one('product.product', string='Product', store=True)
    
    @api.onchange('package_id')
    def _onchange_package_id(self):
        self.product_id = self.package_id and self.package_id.product_id or False

    @api.depends('move_line_ids')
    def _compute_qty_done(self):
        for each in self:
            each.qty_done = sum(each.move_line_ids.filtered(lambda ml:ml.state == 'done').mapped('qty_done'))
