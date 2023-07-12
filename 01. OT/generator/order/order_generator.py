from common.generator import Generator
from models.order import Order

import calendar
import datetime
import random
import uuid

class OrderGenerator(Generator):
    def __init__(self):
        self.year = random.randint(2020, 2023) 
        self.month = random.randint(1,12)

    def generator(self):
        Order_id = uuid.uuid4()
        orderAt = random.randint(1,calendar.monthrange(self.year, self.month)[1])

        