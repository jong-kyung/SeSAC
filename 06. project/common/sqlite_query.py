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
    
    # TODO: 데이터를 한번에 보내는것보다 LIMIT 걸어서 보내주자.
    # TODO: 페이지네이션은 count로 쿼리요청을 해서 갯수를 구해보는거로
    # TODO: 인덱싱 해주는 것 말고 더 좋은 방법은 없을까? for 문을 돌린다던지..

    def total_data_query(self, page, count, *args):
        condition = []
        find_data = []
        for i in range(len(args)):
            if i%2 == 0 :
                condition.append(args[i])
            else:
                find_data.append(args[i])
         
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()
        # -------- 원하는 data 불러오기 --------
        cursor.execute(f"SELECT * FROM {self.TableName} WHERE {condition[0]} LIKE ? AND {condition[1]} LIKE ? LIMIT {count} OFFSET {(page - 1)*count}" , ( find_data[0]+ '%', find_data[1] + '%'))
        datas = cursor.fetchall()
        print(datas)
        #  -------- 원하는 data 길이 불러오기 --------
        cursor.execute(f"SELECT count(*) FROM {self.TableName} WHERE {condition[0]} LIKE ? AND {condition[1]} LIKE ?" , ( find_data[0]+ '%', find_data[1] + '%'))
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