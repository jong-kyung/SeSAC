from user.user_generator import UserGenerator
from store.store_generator import StoreGenerator

def user_generator(count):
    user = UserGenerator()

    users = []
    for _ in range(count):
        data = user.generate_data()
        users.append(data)
    
    return users

def store_generator(count):
    store = StoreGenerator()

    stores = []
    for _ in range(count):
        data = store.generate_data()
        stores.append(data)

    return stores

if __name__ == '__main__': # 메인함수에서 실행할 것
    print(store_generator(10)[0]) # user 입출력 테스트
    # TODO : 모듈화