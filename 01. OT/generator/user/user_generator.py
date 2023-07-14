# 메인함수가 실행되는 위치 기준으로 절대경로 설정, 내가 작성한 메인함수에서는 generator 에서 작동하는 함수이므로 generator를 기준으로 하위 경로를 작성해주면 된다.
from common.generator import Generator
from user.user_name_generator import NameGenerator
from user.birthdate_generator import BirthdateGenerator
from user.gender_generator import GenderGenerator
from common.address_generator import AddressGenerator
from models.user import User
import uuid
class UserGenerator(Generator):
    def __init__(self):
        self.user_name_gen = NameGenerator()
        self.birthdate_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generator(self):
        user_id = uuid.uuid4()
        user_name =  self.user_name_gen.generate_name()
        birthdate = self.birthdate_gen.generate_birthdate()
        gender = self.gender_gen.generate_gender()
        address = self.address_gen.generate_address()[0]
        
        return User(user_id, user_name, gender, birthdate, address).get_info()
