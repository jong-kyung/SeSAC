import random
import os
class NameGenerator:
    def __init__(self):
        self.name = []
        self.path = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 절대경로 구하기

        with open(f'{self.path}/names.txt') as file:
            names = file.readlines()
        for name in names:
            self.name.append(name.strip())
    
    def generate_name(self):
        return random.choice(self.name)
