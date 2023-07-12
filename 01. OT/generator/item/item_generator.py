from common.generator import Generator
from models.item import Item

import uuid
import random

class ItemGenerator(Generator):
    def __init__(self):
        self.item_types = {
            "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }

    def generator(self):
        item_id = uuid.uuid4()
        item_type = random.choice(list(self.item_types.keys()))
        item_subtype = random.choice(list(self.item_types[item_type].keys()))
        item_name = f"{item_subtype} {item_type}"
        item_price = self.item_types[item_type][item_subtype]
        return Item(item_id, item_name, item_type, item_price).get_info()