import sqlite3

# TODO : 상속기능으로 클래스를 두개 만드는것도 괜찮을듯함 DB를 고르는거 하나, 쿼리요청 하나
class SQLite3_connect:
    def __init__(self, DB_Name):
        self.connection = sqlite3.connect(f'./DB/{DB_Name}.db')
        self.cursor = self.connection.cursor()
        self.DB_Name = DB_Name

