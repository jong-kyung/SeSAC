class User:
    def __init__(self, name, gender, birthdate, address):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address

    def __str__(self): # 객체의 정보를 사용자에게 보여주기 위한 함수
        return f"Name: {self.name}, Gender: {self.gender} Birthdate: {self.birthdate}, Address: {self.address}"
    