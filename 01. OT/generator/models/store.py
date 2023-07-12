class Store:
    def __init__(self, store_id, store_type, name, address):
        self.store_id = store_id
        self.name = name
        self.store_type = store_type
        self.address = address
    
    def __str__(self): 
        return f"{self.store_id}, {self.store_type}, {self.name}, {self.address}"
    
    def get_info(self):
        return {
            'id' : self.store_id,
            'name' : self.name,
            'type' : self.store_type,
            'address' : self.address
        }
    