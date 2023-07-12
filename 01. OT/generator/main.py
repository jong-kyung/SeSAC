from control_data import generate_data

import csv

def find_id(FileName):
    id_datas = []
    with open(f'./csv/{FileName}s.csv', 'r', newline='') as file:
        csv_file = csv.reader(file)
        for data in csv_file:
            print(data[0])


if __name__ == '__main__': # 메인함수에서 실행할 것
    data_type = input('데이터 유형을 입력하세요 (User, Store 또는 Item)')
    data_count = input('생성할 데이터 개수를 입력하세요')
    data_output_type = input('아웃풋 형태를 입력하세요(csv, console)')
    my_data = generate_data(data_type, data_count, data_output_type)
    
    my_data.data_generator()

    # find_id('user')