from sql.sqlite_connect import SQLite3_connect

class Store_query(SQLite3_connect):   
    def __init__(self, DB_Name, TableName):
        super().__init__(DB_Name)
        self.TableName = TableName

    def schema_query(self):
        headers = []
        # -------- schema 불러오기 --------
        self.cursor.execute(f"PRAGMA table_info({self.TableName})")
        schemas = self.cursor.fetchall()
        for schema in schemas:  
            headers.append(schema[1]) # schema 값 선택
        return headers
    
    def total_data_query(self, page, count, *args):
        conditions = []
        find_datas = []
        condition_query = ''
        find_data_query = ()
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
        for find_data in find_datas:
            find_data_query += (f'%{find_data}%',)

        # -------- 원하는 data 전체 불러오기 --------
        self.cursor.execute(f"SELECT * FROM {self.TableName} WHERE {condition_query} LIMIT {count} OFFSET {(page - 1)*count}" , find_data_query)
        datas = self.cursor.fetchall()
        #  -------- 원하는 data 길이 불러오기 --------
        self.cursor.execute(f"SELECT count(*) FROM {self.TableName} WHERE {condition_query}" , find_data_query)
        data_length = self.cursor.fetchone()[0]

        return {'datas':datas, 'data_length': data_length}

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

# TODO : 각 매장별 연매출 출력하는 쿼리문 작성하기
    def monthly_sale(self, store_ID):
        self.cursor.execute(f'''SELECT substr(orders.OrderAt,1,7) AS Month, SUM(items.price) AS Revenue FROM {self.TableName} 
                            INNER JOIN orders ON {self.TableName}.Id = orders.StoreId 
                            INNER JOIN orderitems ON orders.Id = orderitems.OrderId 
                            INNER JOIN items ON orderitems.ItemId = items.Id WHERE stores.Id = ? 
                            GROUP BY stores.Name, Month 
                            ORDER BY Month''', (store_ID,))
        result = self.cursor.fetchall()

        return result