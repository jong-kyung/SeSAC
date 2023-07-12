from common.generator import Generator
from models.order import Order
from common.find_row import find_row

import calendar
import random
import uuid

class OrderGenerator(Generator):
    def __init__(self):
        self.year = random.randint(2020, 2023) 
        self.month = random.randint(1,12)
        self.StoreId = find_row('store','Id')
        self.UserId = find_row('user', 'Id')

    def generator(self):
        order_id = uuid.uuid4()
        OrderAt = random.randint(1,calendar.monthrange(self.year, self.month)[1])
        StoreId = random.choice(self.StoreId)
        UserId = random.choice(self.UserId)

        return Order(order_id, OrderAt, StoreId, UserId).get_info()


        