from control_data import generate_data

if __name__ == '__main__': # 메인함수에서 실행할 것
    data_type = input('데이터 유형을 입력하세요 (User, Store, Item, Order, OrderItem)')
    data_count = input('생성할 데이터 개수를 입력하세요')
    data_output_type = input('아웃풋 형태를 입력하세요(csv, console)')
    my_data = generate_data(data_type, data_count, data_output_type)
    
    my_data.user_request()