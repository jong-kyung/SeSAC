class OrderItem:
    def __init__(self, order_id, OrderId, ItemId):
        self.item_id = order_id
        self.OrderId = OrderId
        self.ItemId = ItemId

    def __str__(self):
        return f'{self.item_id}, {self.OrderId}, {self.ItemId}'

    def get_info(self):
        return {
            'Id' : self.item_id,
            'OrderId': self.OrderId,
            'ItemId' : self.ItemId
        }