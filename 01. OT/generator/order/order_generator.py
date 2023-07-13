from common.generator import Generator
from models.order import Order
from common.find_row import find_row

from datetime import datetime, timedelta
import random
import uuid

class OrderGenerator(Generator):
    def __init__(self):
        self.StoreId = find_row('store','Id')
        self.UserId = find_row('user', 'Id')

    def generator(self):
        order_id = uuid.uuid4()
        start = datetime(2023, 1, 1)  # 범위의 시작 날짜
        end = datetime(2023, 12, 31)  # 범위의 끝 날짜

        # 범위 내에서 랜덤한 날짜 생성
        time_difference = end - start
        random_seconds = random.randint(0, time_difference.total_seconds())
        OrderAt = start + timedelta(seconds=random_seconds)
        StoreId = random.choice(self.StoreId)
        UserId = random.choice(self.UserId)

        return Order(order_id, OrderAt, StoreId, UserId).get_info()


        