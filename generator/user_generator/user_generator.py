 # 메인함수가 실행되는 위치 기준으로 절대경로 설정, 내가 작성한 메인함수에서는 generator 에서 작동하는 함수이므로 generator. 이 아닌 하위 경로로 작성해주면 된다.
from user_generator.user_name_generator import NameGenerator
from user_generator.birthdate_generator import BirthdateGenerator
from user_generator.gender_generator import GenderGenerator
from common.address_generator import AddressGenerator
from models.user import User
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
        
        return User(user_name, gender, birthdate, address)
    
