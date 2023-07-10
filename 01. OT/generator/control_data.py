from user.user_generator import UserGenerator
from store.store_generator import StoreGenerator
import csv

class generate_data:
    def __init__(self, data_type, count, output):
        self.data_result= []
        self.data_type = data_type.lower()
        self.count = int(count)
        self.output = output.lower()
        # TODO : 메인 함수 혹은 새로운 함수로 변수값 유형을 검사하는 것으로 변경

    def user_request(self):
        self.data_generator()
        self.print_data()
        return print('작업이 완료되었습니다.')

    # TODO : 코드 간소화
    def data_generator(self):
        datas = ['user', 'store', 'item']
        if self.data_type == datas[0]:
            self.data_result = self.user_generator()
        elif self.data_type == datas[1]:
            self.data_result = self.store_generator()
        # else:
        #     self.item_generator()
        # self.print_data()

        return self.data_result
        
    def user_generator(self):
        data = []
        user = UserGenerator()

        for _ in range(self.count):
            user_info = user.generator()
            data.append(user_info)

        return data

    def store_generator(self):
        data = []
        store = StoreGenerator()

        for _ in range(self.count):
            store_info = store.generator()
            data.append(store_info)

        return data
    
    def print_data(self):
        outputs = ['console', 'csv']
        if self.output == outputs[0]:
            self.print_console()
        elif self.output == outputs[1]:
            self.print_csv()
    
    def print_csv(self):
        with open(f'{self.data_type}.csv', 'a') as file:
            csv_file = csv.writer(file)
            csv_file.writerow(self.data_result)
            print('요청된 데이터 파일 생성 중..')

    def print_console(self):
        for data in self.data_result:
            print(data)