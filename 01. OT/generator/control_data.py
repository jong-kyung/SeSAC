from user.user_generator import UserGenerator
from store.store_generator import StoreGenerator
from item.item_generator import ItemGenerator
from order.order_generator import OrderGenerator
from orderitem.orderitem_generator import OrderItemGenerator
import csv

class generate_data:
    def __init__(self, data_type, count, output):
        self.data_result= []
        self.data_type = data_type.lower()
        self.count = int(count)
        self.output = output.lower()
        self.fieldname = []
        # TODO : 메인 함수 혹은 새로운 함수로 변수값 유형을 검사하는 것으로 변경

    def user_request(self):
        self.data_generator()
        self.print_data()

    # TODO : 코드 간소화
    def data_generator(self):
        datas = ['user', 'store', 'item', 'order', 'orderitem']
        if self.data_type == datas[0]:
            self.data_result = self.user_generator()
        elif self.data_type == datas[1]:
            self.data_result = self.store_generator()
        elif self.data_type == datas[2]:
            self.data_result = self.item_generator()
        elif self.data_type == datas[3]:
            self.data_result = self.order_generator()
        elif self.data_type == datas[4]:
            self.data_result = self.orderitem_generator()
        
    def user_generator(self):
        self.fieldname = ['Id','Name','Gender','Birthdate','Address']
        data = []
        user = UserGenerator()
        for _ in range(self.count):
            user_info = user.generator()
            data.append(user_info)

        return data

    def store_generator(self):
        self.fieldname = ['Id','Name','Type','Address']
        data = []
        store = StoreGenerator()

        for _ in range(self.count):
            store_info = store.generator()
            data.append(store_info)

        return data
    
    def item_generator(self):
        self.fieldname = ['Id','Name','Type','Price']
        data = []
        item = ItemGenerator()

        for _ in range(15):
            item_info = item.generator()
            data.append(item_info)

        return data
    
    def order_generator(self):
        self.fieldname = ['Id','OrderAt','StoreId','UserId']
        data = []
        order = OrderGenerator()

        for _ in range(self.count):
            order_info = order.generator()
            data.append(order_info)

        return data
    
    def orderitem_generator(self):
        self.fieldname =['Id', 'OrderId', 'ItemId']
        data = []
        orderitem = OrderItemGenerator()

        for _ in range(self.count):
            orderitem_info = orderitem.generator()
            data.append(orderitem_info)
        
        return data

    def print_data(self):
        outputs = ['console', 'csv']
        if self.output == outputs[0]:
            self.print_console()
        elif self.output == outputs[1]:
            self.print_csv(self.fieldname)
    
    def print_csv(self, param):
        with open(f'./csv/{self.data_type}s.csv', 'w', newline='') as file:
            csv_file = csv.DictWriter(file, fieldnames = param)
            csv_file.writeheader()
            csv_file.writerows(self.data_result)
            
        print('파일 생성 완료')

    def print_console(self):
        for data in self.data_result:
            print(data)