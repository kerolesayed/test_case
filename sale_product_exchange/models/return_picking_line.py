from odoo import fields, models


class StockReturnPickingLineInherit(models.TransientModel):
    _inherit = 'stock.return.picking.line'

    exchange_product_id = fields.Many2one('product.product')
