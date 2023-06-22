class User:
    def __init__(self, user_id, name, gender, birthdate, address):
        self.user_id = user_id
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address

    def __str__(self): # 객체의 정보를 사용자에게 보여주기 위한 함수
        return f"ID: {self.user_id} Name: {self.name}, Gender: {self.gender} Birthdate: {self.birthdate}, Address: {self.address}"
    