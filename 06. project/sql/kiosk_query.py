from sql.sqlite_connect import SQLite3_connect

class Kiosk_query(SQLite3_connect):
    def __init__(self, DB_Name):
        super().__init__(DB_Name)

    def result_query(self, store_id, item_id):
        self.cursor.execute(f"SELECT Name, Price FROM items WHERE Id = ?", (item_id,))
        item_info = self.cursor.fetchall()
        
        self.cursor.execute(f"SELECT Name FROM stores WHERE Id = ?",(store_id,))
        store_info = self.cursor.fetchall()
        
        result = item_info + store_info

        return result