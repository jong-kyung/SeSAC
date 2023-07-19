import uuid
import datetime

from sql.sqlite_connect import SQLite3_connect
class Kiosk_query(SQLite3_connect):
    def __init__(self, DB_Name):
        super().__init__(DB_Name)

    def insert_data(self, item_info, store_id, user_id):
        for item in item_info:
            print(item['id'])
        # orders : id / orderat / storeid / userid 1번만 생성
        # orderitem : id / orderid / itemid 아이템 갯수만큼 생성

