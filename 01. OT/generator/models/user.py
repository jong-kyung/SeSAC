class User:
    def __init__(self, user_id, name, gender, birthdate, address):
        self.user_id = user_id
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address
    
    def __str__(self): # 객체의 정보를 사용자에게 보여주기 위한 함수, print로 출력할때만 작동함
        return f"{self.user_id}, {self.name}, {self.gender}, {self.birthdate}, {self.address}"
    
    def get_info(self):
        return f"{self.user_id}, {self.name}, {self.gender}, {self.birthdate}, {self.address}"