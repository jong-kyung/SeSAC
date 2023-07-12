class Order:
    def __init__(self, order_id, orderAt, StoreId, UserId):
        self.item_id = order_id
        self.orderAt = orderAt
        self.StoreId = StoreId
        self.UserId = UserId

    def __str__(self):
        return f'{self.item_id}, {self.orderAt}, {self.StoreId}, {self.UserId}'

    def get_info(self):
        return f'{self.item_id}, {self.orderAt}, {self.StoreId}, {self.UserId}'