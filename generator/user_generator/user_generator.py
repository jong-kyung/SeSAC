from .user_name_generator import NameGenerator
from .birthdate_generator import BirthdateGenerator
from .gender_generator import GenderGenerator
from generator.common.address_generator import AddressGenerator

from ..models.user import User
class UserGenerator:
    def __init__(self):
        self.user_name_gen = NameGenerator()
        self.birthdate_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()


    def generate_data(self):
        user_name =  self.user_name_gen.generate_name()
        birthdate = self.birthdate_gen.generate_birthdate()
        gender = self.gender_gen.generate_gender()
        address = self.address_gen.generate_address()[0]
        append_data = user_name,birthdate,gender,address
        
        return User(append_data)
    
