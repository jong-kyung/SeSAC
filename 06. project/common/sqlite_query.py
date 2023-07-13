import sqlite3

class SQLite3_query():
    def __init__(self, TableName):
        self.headers = []
        self.TableName = TableName
    
    def schema_query(self):
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()
        # -------- schema 불러오기 --------
        cursor.execute(f"PRAGMA table_info({self.TableName})")
        schemas = cursor.fetchall()
        for schema in schemas:  
            self.headers.append(schema[1]) # schema 값 선택

        return self.headers

    def total_data_query(self):
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()
        
        # -------- data 불러오기 --------
        cursor.execute(f"SELECT * FROM {self.TableName}")
        datas = cursor.fetchall()
        return  datas
    
    def detail_info(self, FindData):
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {self.TableName} WHERE Id = ?", [FindData])
        result = cursor.fetchone()

        return result

    def check_overlap(self, param):
        conn = sqlite3.connect('./DB/auth.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT Id FROM {self.TableName} WHERE username = ?", (param, ))
        user_id = cursor.fetchone()

        return user_id
    
    def insert_user(self, param):
        conn = sqlite3.connect('./DB/auth.db')
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO {self.TableName}(UserName, Password) VALUES (?, ?)", param)
        conn.commit()
        conn.close()

    def user_auth(self, id, pw):
        conn = sqlite3.connect('./DB/auth.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT UserName, Password FROM {self.TableName} WHERE UserName = ? AND Password = ?", (id, pw))
        result = cursor.fetchone()
        print(result)
        return result