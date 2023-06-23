from store.store_name_generator import NameGenerator
from common.address_generator import AddressGenerator
from common.generator import Generator
from models.store import Store

import uuid

class StoreGenerator(Generator):
    def __init__(self):
        self.store_name = NameGenerator()
        self.address = AddressGenerator()

    def generator(self):
        store_id = uuid.uuid4()
        store_name = self.store_name.generate_name()
        address = self.address.generate_address()[0]
        store_info = f'{store_name} {self.address.generate_address()[1]}'

        return Store(store_id, store_info, store_name, address)
        