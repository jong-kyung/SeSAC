import sqlite3

# TODO : 상속기능으로 클래스를 두개 만드는것도 괜찮을듯함 DB를 고르는거 하나, 쿼리요청 하나
class SQLite3_connect:
    def __init__(self, DB_Name ,TableName):
        self.headers = []
        self.TableName = TableName
        self.conn = sqlite3.connect(f'./DB/{DB_Name}')
        self.cursor = self.conn.cursor()
    
    def schema_query(self):
        # -------- schema 불러오기 --------
        self.cursor.execute(f"PRAGMA table_info({self.TableName})")
        schemas = self.cursor.fetchall()
        for schema in schemas:  
            self.headers.append(schema[1]) # schema 값 선택

        return self.headers
