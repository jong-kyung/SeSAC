import random

class AddressGenerator:
    def __init__(self):
        self.cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

    def generate_address(self):
        street = random.randint(1,100)
        city = random.choice(self.cities)
        return f'{street} {city}'
