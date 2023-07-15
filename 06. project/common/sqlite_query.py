import sqlite3

# TODO : 상속기능으로 클래스를 두개 만드는것도 괜찮을듯함 DB를 고르는거 하나, 쿼리요청 하나
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
    
    def total_data_query(self, page, count):
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()
        # -------- 원하는 data 전체 불러오기(order, orderitem) --------
        cursor.execute(f"SELECT * FROM {self.TableName} LIMIT {count} OFFSET {(page-1)*count}")
        datas = cursor.fetchall()
        #  -------- 원하는 data 길이 불러오기 --------
        cursor.execute(f"SELECT count(*) FROM {self.TableName}")
        data_length = cursor.fetchone()[0]

        return {'datas':datas, 'data_length': data_length}
    
    def condition_data_query(self, page, count, *args):
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
        # TODO 인덱싱을해서 마지막을 지우는 것은 어떨지?
        for num in range(len(conditions)):
            if num == len(conditions) - 1: 
                condition_query += f'{conditions[num]} LIKE ?'
            else:
                condition_query += f'{conditions[num]} LIKE ? AND '

        # 검색내용 튜플에 넣기
        for find_data in find_datas:
            find_data_query += ('%' + find_data + '%',)

        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()
        # -------- 원하는 data 전체 불러오기(user, store, item) --------
        cursor.execute(f"SELECT * FROM {self.TableName} WHERE {condition_query} LIMIT {count} OFFSET {(page - 1)*count}" , find_data_query)
        datas = cursor.fetchall()
        #  -------- 원하는 data 길이 불러오기 --------
        cursor.execute(f"SELECT count(*) FROM {self.TableName} WHERE {condition_query}" , find_data_query)
        data_length = cursor.fetchone()[0]

        return {'datas':datas, 'data_length': data_length}

    def find_data_query(self, column):
        result_datas = []
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT DISTINCT {column} FROM {self.TableName}")
        datas = cursor.fetchall()
        for data in datas:
            result_datas.append(data[0])
        return result_datas

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