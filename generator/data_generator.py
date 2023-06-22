import csv
import os
from user_generator import user_name_generator
from user_generator import birthdate_generator
from user_generator import gender_generator
from common import address_generator
from store_generator import store_name_generator

class DataGenerator:
    def __init__(self):
        self.user_name_gen = user_name_generator.NameGenerator()
        self.birthdate_gen = birthdate_generator.BirthdateGenerator()
        self.gender_gen = gender_generator.GenderGenerator()
        self.store_name_gen = store_name_generator.NameGenerator()
        self.address_gen = address_generator.AddressGenerator()
        self.data_type = ['user','store']
        self.output_data = ['stdout', 'csv', 'console']
        self.request_data = input('데이터 유형을 입력하세요(User, Store 또는 Item)').lower()
        self.request_count = int(input('생성할 데이터 개수를 입력하세요:'))
        self.request_output = input('아웃풋 형태를 입력하세요.').lower()
        # super().__imit__()부모의 instance 속성값 받아오기

    def generate_data(self):
        result_data = []

        if  self.request_data in self.data_type:
            if self.request_data == self.data_type[0]:
                for _ in range(self.request_count):
                    user_name =  self.user_name_gen.generate_name()
                    birthdate = self.birthdate_gen.generate_birthdate()
                    gender = self.gender_gen.generate_gender()
                    address = self.address_gen.generate_address()[0]
                    append_user = (user_name, birthdate, gender, address)

                    result_data.append(append_user)
            elif self.request_data == self.data_type[1]:
                for _ in range (self.request_count):
                    store_name = self.store_name_gen.generate_name()
                    store_info = f'{store_name} {self.address_gen.generate_address()[1]}'
                    address = self.address_gen.generate_address()[0]
                    append_store = (store_info, store_name, address)

                    result_data.append(append_store)
        
        return result_data
    

    def output_requested_data(self):
        if self.request_output in self.output_data:
            if self.request_output == self.output_data[1]:
                self.Write_data()
            else:
                self.Write_console()
            
    
    def Write_data(self):
        data = self.generate_data()
        user_headers = ['Name', 'Birthdate', 'Gender', 'Address']
        store_headers = ['Name', 'Name', 'Address']
        
        if self.request_data in self.data_type:
            if self.request_data == self.data_type[0]:
                with open('user.csv', 'a', newline='\n') as file: 
                    csv_file = csv.writer(file)
                    csv_file.writerow(user_headers)
                    csv_file.writerows(data)
                    print('User 데이터 생성완료')
            elif self.request_data == self.data_type[1]:
                with open('store.csv', 'a', newline='\n') as file:
                    csv_file = csv.writer(file)
                    csv_file.writerow(store_headers)
                    csv_file.writerows(data)
                    print('Store 데이터 생성완료')

    def Write_console(self):
        data = self.generate_data()
        for dat in data:
            print(dat)

data1 = DataGenerator()

data1.output_requested_data()