import random

class NameGenerator:
    def __init__(self):
        self.first_names = []
        self.last_names = []
        with open('first_names.txt') as file:
            first_names = file.readlines()
        for first_name in first_names:
            self.first_names.append(first_name.strip())

        with open('last_names.txt') as file:
            last_names = file.readlines()
        for last_name in last_names:
            self.last_names.append(last_name.strip())
        

    def generate_name(self):
        user_name = random.choice(self.last_names) + random.choice(self.first_names)
        return user_name