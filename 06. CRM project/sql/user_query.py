from sql.sqlite_connect import SQLite3_connect

class User_query(SQLite3_connect):   
    def __init__(self, DB_Name, TableName):
        super().__init__(DB_Name)
        self.TableName = TableName
    
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
        # TODO : 인덱싱을해서 마지막을 지우는 것은 어떨지?
        # TODO : Kwargs 로 받아서 처리하는게 코드의 흐름을 파악하기 좋을 듯 함.
        for num in range(len(conditions)):
            if num == len(conditions) - 1: 
                condition_query += f'{conditions[num]} LIKE ?'
            else:
                condition_query += f'{conditions[num]} LIKE ? AND '

        # 검색내용 튜플에 넣기
        # TODO 비효율적인거같은데 고쳐야할듯?
        for i in range(len(find_datas)):
            if i == 1:
                find_data_query += (f'{find_datas[i]}%',)
            else:
                find_data_query += (f'%{find_datas[i]}%',)


        # 원하는 data 전체 불러오기
        self.cursor.execute(f"SELECT * FROM {self.TableName} WHERE {condition_query} LIMIT {count} OFFSET {(page - 1)*count}" , find_data_query)
        datas = self.cursor.fetchall()
        
        # 원하는 data 길이 불러오기
        self.cursor.execute(f"SELECT count(*) FROM {self.TableName} WHERE {condition_query}" , find_data_query)
        data_length = self.cursor.fetchone()[0]

        return {'datas': datas, 'data_length': data_length}


    # TODO : dictionary 로 받는걸로 고치거나 튜플로 사용할경우엔 왜 인덱싱을 해주었는지 주석을 달아줄 것
    def find_data_query(self, column):
        result_datas = []

        self.cursor.execute(f"SELECT DISTINCT {column} FROM {self.TableName}")
        datas = self.cursor.fetchall()
        for data in datas:
            result_datas.append(data[0])
        return result_datas

    def detail_info(self, FindData):
        self.cursor.execute(f"SELECT * FROM {self.TableName} WHERE Id = ?",(FindData,))
        result = self.cursor.fetchone()

        return result
    
    def store_rate(self, UserID):
        self.cursor.execute(f'''
                            SELECT stores.Id ,stores.Name, count(orders.Id) AS count FROM stores 
                            INNER JOIN orders ON stores.Id = orders.StoreId
                            INNER JOIN orderitems ON orders.Id = orderitems.OrderId
                            INNER JOIN {self.TableName} ON orders.UserId = {self.TableName}.Id WHERE {self.TableName}.Id = '{UserID}'
                            GROUP BY stores.Name 
                            ORDER BY count DESC
                            LIMIT 5''')
        result = self.cursor.fetchall()

        return result