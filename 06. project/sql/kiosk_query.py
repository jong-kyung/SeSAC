import uuid
import datetime

from sql.sqlite_connect import SQLite3_connect, sqlite3
class Kiosk_query(SQLite3_connect):
    def __init__(self, DB_Name):
        super().__init__(DB_Name)

    def insert_datas(self, item_info ,store_id, user_id):
        OrderId = uuid.uuid4()
        today = datetime.datetime.now() # 오늘 날짜
        OrderAt = today.strftime('%Y-%m-%d %H:%M:%S') # DB와 맞춰주기
        # orders 에 데이터 삽입 
        self.cursor.execute('INSERT INTO orders (Id, OrderAt, StoreId, UserID) VALUES (?, ?, ?, ?)', (str(OrderId), OrderAt, store_id, user_id))

        # orderitems 에 데이터 삽입
        for i in range(len(item_info)): # 각 행만큼 반복
            for k in range(int(item_info[i]['count'])): # 중복 상품 갯수만큼 반복
                OrderItemId = uuid.uuid4()
                self.cursor.execute('INSERT INTO orderitems (Id, OrderId, ItemId) VALUES (?, ?, ?)', (str(OrderItemId), str(OrderId), item_info[i]['id']))
        self.connection.commit()
        self.connection.close()

def find_user_id(user_name):
    connection = sqlite3.connect('./DB/auth.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM users WHERE Username = ?',(user_name,))
    user_id = cursor.fetchone()
    
    return user_id[0]