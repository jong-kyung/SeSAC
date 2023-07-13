from common.generator import Generator
from models.orderitem import OrderItem
from common.find_row import find_row

import random
import uuid

class OrderItemGenerator(Generator):
    def __init__(self):
        self.OrderId = find_row('order', 'Id')
        self.ItemId = find_row('item', 'Id')

    def generator(self):
        OrderItem_id = uuid.uuid4()
        OrderId = random.choice(self.OrderId)
        ItemId = random.choice(self.ItemId)

        return OrderItem(OrderItem_id, OrderId, ItemId).get_info()


        