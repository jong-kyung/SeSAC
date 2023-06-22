import random

class NameGenerator:
    def __init__(self):
        self.names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
    def generate_name(self):
        return random.choice(self.names)