import random
import os

class AddressGenerator:
    def __init__(self):
        self.cities = []
        self.sub_address = []
        self.path = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 절대경로 구하기
        with open(f'{self.path}/cities.txt') as file:
            cities = file.readlines()
        for city in cities:
            self.cities.append(city.strip())
        
        with open(f'{self.path}/sub_address.txt') as file:
            sub_address = file.readlines()
        for sub in sub_address:
            self.sub_address.append(sub.strip())

    def generate_address(self):
        city = random.choice(self.cities)
        sub = random.choice(self.sub_address)
        street1 = random.randint(1, 100)
        street2 = random.randint(1, 100)
        return f'{city} {sub} {street1}길 {street2}' , f'{sub} {street2}호점' # 호점 -> 변수로 바꿔야함 (언어마다 다르게 해줘야하기 때문)
        
