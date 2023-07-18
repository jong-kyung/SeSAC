from sql.sqlite_connect import SQLite3_connect

class Kiosk_query(SQLite3_connect):
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