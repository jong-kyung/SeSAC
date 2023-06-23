import random
import os

class NameGenerator:
    def __init__(self):
        self.first_names = []
        self.last_names = []
        
        self.path = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 절대경로 구하기
        with open(f'{self.path}/first_names.txt') as file:
            first_names = file.readlines()
        for first_name in first_names:
            self.first_names.append(first_name.strip())

        with open(f'{self.path}/last_names.txt') as file:
            last_names = file.readlines()
        for last_name in last_names:
            self.last_names.append(last_name.strip())
        

    def generate_name(self):
        user_name = random.choice(self.last_names) + random.choice(self.first_names)
        return user_name