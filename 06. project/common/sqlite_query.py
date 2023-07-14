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
    
    def total_data_query(self, page, count, *args):
        conditions = []
        find_datas = []
        condition_query = ''
        find_data_query = ()

        # 조건과 검색내용 분류
        for i in range(len(args)):
            if i%2 == 0 :
                conditions.append(args[i])
            else:
                find_datas.append(args[i])
                
        # 조건의 갯수에 따라 AND 붙여주기
        for num in range(len(conditions)):
            if num == len(conditions) - 1: 
                condition_query += f'{conditions[num]} LIKE ?'
            else:
                condition_query += f'{conditions[num]} LIKE ? AND '

        # 검색내용 튜플에 넣기
        for find_data in find_datas:
            find_data_query += (find_data + '%',)

        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()
        # -------- 원하는 data 불러오기 --------
        cursor.execute(f"SELECT * FROM {self.TableName} WHERE {condition_query} LIMIT {count} OFFSET {(page - 1)*count}" , find_data_query)
        datas = cursor.fetchall()
        #  -------- 원하는 data 길이 불러오기 --------
        cursor.execute(f"SELECT count(*) FROM {self.TableName} WHERE {condition_query}" , find_data_query)
        data_length = cursor.fetchone()[0]

        return {'datas':datas, 'data_length': data_length}

    def detail_info(self, FindData):
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {self.TableName} WHERE Id = ?",(FindData,))
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