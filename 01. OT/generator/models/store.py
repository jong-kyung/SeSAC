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
            'Id' : self.store_id,
            'Name' : self.name,
            'Type' : self.store_type,
            'Address' : self.address
        }
    