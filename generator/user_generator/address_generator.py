import random

class AddressGenerator:
    def __init__(self):
        self.cities = []
        self.sub_address = []
        with open('cities.txt') as file:
            cities = file.readlines()
        for city in cities:
            self.cities.append(city.strip())
        
        with open('sub_address.txt') as file:
            sub_address = file.readlines()
        for sub in sub_address:
            self.sub_address.append(sub.strip())

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.choice(self.sub_address)
        return f'{city} {street}'
