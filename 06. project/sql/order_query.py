import sqlite3
from sql.sqlite_connect import SQLite3_connect

class Order_query(SQLite3_connect):   
    def total_data_query(self, page, count):
        # -------- 원하는 data 전체 불러오기(order, orderitem) --------
        self.cursor.execute(f"SELECT * FROM {self.TableName} LIMIT {count} OFFSET {(page-1)*count}")
        datas = self.cursor.fetchall()
        #  -------- 원하는 data 길이 불러오기 --------
        self.cursor.execute(f"SELECT count(*) FROM {self.TableName}")
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
        conn = sqlite3.connect('./DB/crm.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {self.TableName} WHERE Id = ?",(FindData,))
        result = cursor.fetchone()

        return result