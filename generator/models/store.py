class Store:
    def __init__(self, store_id, store_info, name, address):
        self.store_id = store_id
        self.store_info = store_info
        self.name = name
        self.address = address
    
    def __str__(self): 
        return f"{self.store_id}, {self.store_info}, {self.name}, {self.address}"
    