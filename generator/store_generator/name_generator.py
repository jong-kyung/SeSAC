import random

class NameGenerator:
    def __init__(self):
        self.name = []

        with open('names.txt') as file:
            names = file.readlines()
        for name in names:
            self.name.append(name.strip())
    
    def generate_name(self):
        return random.choice(self.name)
    
name=NameGenerator()
print(name.generate_name())