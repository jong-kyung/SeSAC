from store.store_name_generator import NameGenerator
from common.address_generator import AddressGenerator
from common.generator import Generator
from models.store import Store

import uuid

class StoreGenerator(Generator):
    def __init__(self):
        self.store_type = NameGenerator()
        self.address = AddressGenerator()

    def generator(self):
        store_id = uuid.uuid4()
        store_type = self.store_type.generate_name()
        total_adress = self.address.generate_address()
        address = total_adress[0]
        store_name = f'{store_type} {total_adress[1]}'

        return Store(store_id, store_name, store_type, address).get_info()
        