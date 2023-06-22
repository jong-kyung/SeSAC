import csv
import os
from user_generator import name_generator
from user_generator import birthdate_generator
from user_generator import gender_generator
from address import address_generator

class DataGenerator:
    def __init__(self):
        self.name_gen = name_generator.NameGenerator()
        self.birthdate_gen = birthdate_generator.BirthdateGenerator()
        self.gender_gen = gender_generator.GenderGenerator()
        self.address_gen = address_generator.AddressGenerator()
        self.headers = ['Name', 'Birthdate', 'Gender', 'Address']
        # super().__imit__()부모의 instance 속성값 받아오기

    def generate_data(self, count):
        data = []
        for _ in range(count):
            name =  self.name_gen.generate_name()
            birthdate = self.birthdate_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()

            data.append((name, birthdate, gender, address))
            
        return data
    
    def Write_data(self, count):
        data = self.generate_data(count)
        with open('user.csv', 'a', newline='\n') as file: # \n : newline, \r : linefeed
            csv_file = csv.writer(file)
            csv_file.writerow(self.headers)
            csv_file.writerows(data)

    def Write_console(self, count):
        data = self.generate_data(count)
        for dat in data:
            print(dat)

data1 = DataGenerator()

data1.Write_console(10)