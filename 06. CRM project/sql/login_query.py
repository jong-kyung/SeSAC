from sql.sqlite_connect import SQLite3_connect

class Login_query(SQLite3_connect):
    def __init__(self, DB_Name, TableName):
        super().__init__(DB_Name)
        self.TableName = TableName

    def check_overlap(self, param): # 중복계정 확인
        self.cursor.execute(f"SELECT Username FROM {self.TableName} WHERE Username = ?", (param, ))
        user_id = self.cursor.fetchone()

        return user_id
    
    def insert_user_id(self, user_id): # auth에 사용자 정보 등록
        self.cursor.execute(f"INSERT INTO {self.TableName} (Id, Username, Password) VALUES (?, ?, ?)", user_id)
        self.connection.commit()
        self.connection.close()

    def user_auth(self, id, pw): # 로그인시 사용자 확인
        self.cursor.execute(f"SELECT Username, Password FROM {self.TableName} WHERE Username = ? AND Password = ?", (id, pw))
        result = self.cursor.fetchone()
        self.connection.close()
        
        return result

    def insert_user_info(self, user_info): # crm에 사용자 정보 삽입
        self.cursor.execute(f"INSERT INTO {self.TableName} (Id, Name, Gender, Birthdate, Address) VALUES (?, ?, ?, ?, ?)", user_info)
        self.connection.commit()
        self.connection.close()

    def user_info(self, user_name): # 사용자의 신원에 따라 보여주는 페이지 조절
        self.cursor.execute(f"SELECT Username FROM {self.TableName} WHERE Username = ?", (user_name,))
        result = self.cursor.fetchone()
        self.connection.close()
        
        return result

