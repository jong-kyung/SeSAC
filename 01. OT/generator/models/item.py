class Item:
    def __init__(self, item_id, item_name, item_type, price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_type = item_type
        self.price = price

    def __str__(self):
        return f'{self.item_id}, {self.item_name}, {self.item_type}, {self.price}'

    def get_info(self):
        return f'{self.item_id}, {self.item_name}, {self.item_type}, {self.price}'