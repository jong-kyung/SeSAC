class Store:
    def __init__(self, store_id, store_info, name, address):
        self.store_id = store_id
        self.store_info = store_info
        self.name = name
        self.address = address

    def __str__(self): # 객체의 정보를 사용자에게 보여주기 위한 함수
        return f"ID: {self.store_id} Name: {self.store_info}, Type: {self.name}, Address: {self.address}"
    