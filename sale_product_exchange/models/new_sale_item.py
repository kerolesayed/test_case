from odoo import fields, models


class NewSaleItem(models.TransientModel):
    _name = 'new.sale.item'
    _description = 'ADD Product Line'

    product_id = fields.Many2one('product.product', string="Product", required=True,)
    quantity = fields.Float("Quantity", digits='Product Unit of Measure', required=True,default=1)
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure', related='product_id.uom_id')
    item_id = fields.Many2one('stock.return.picking', string="Wizard")
