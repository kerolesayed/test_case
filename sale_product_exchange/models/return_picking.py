from odoo import models, fields


class ReturnPickingInherit(models.TransientModel):
    _inherit = 'stock.return.picking'

    order_line = fields.One2many('new.sale.item','item_id')

    def create_returns(self):
        if self.order_line and len(self.product_return_moves) != 0:
            res = super().create_returns()
        else:
            res = False
        sale_id = self.picking_id.sale_id
        if any(move.exchange_product_id for move in self.product_return_moves) or self.order_line:
            if sale_id.state == 'done':
                sale_id.action_unlock()

            for line in self.product_return_moves.filtered(lambda x: x.exchange_product_id):
                self.env['sale.order.line'].create({
                    'order_id': line.move_id.sale_line_id.order_id.id,
                    'product_id': line.exchange_product_id.id,
                    'name': line.exchange_product_id.display_name,
                    'product_uom': line.uom_id.id,
                    'product_uom_qty': line.quantity,
                })
            for order in self.order_line:
                self.env['sale.order.line'].create({
                    'order_id': sale_id.id,
                    'product_id': order.product_id.id,
                    'name': order.product_id.display_name,
                    'product_uom': order.uom_id.id,
                    'product_uom_qty': order.quantity,
                })
        return res





