from sql.sqlite_connect import SQLite3_connect

class Kiosk_query(SQLite3_connect):
    def __init__(self, DB_Name):
        super().__init__(DB_Name)

    def result_query(self, data):
        print(data)
        self.cursor.execute()