from sql.sqlite_connect import SQLite3_connect

class Login_query(SQLite3_connect):
    def __init__(self, DB_Name, TableName):
        super().__init__(DB_Name)
        self.TableName = TableName

    def check_overlap(self, param):
        self.cursor.execute(f"SELECT username FROM {self.TableName} WHERE UserName = ?", (param, ))
        user_id = self.cursor.fetchone()

        return user_id
    
    def insert_user_id(self, user_id):
        self.cursor.execute(f"INSERT INTO {self.TableName} (UserName, Password) VALUES (?, ?)", user_id)
        self.connection.commit()
        self.connection.close()

    def user_auth(self, id, pw):
        self.cursor.execute(f"SELECT UserName, Password FROM {self.TableName} WHERE UserName = ? AND Password = ?", (id, pw))
        result = self.cursor.fetchone()
        self.connection.close()
        
        return result

    def insert_user_info(self, user_info):
        self.cursor.execute(f"INSERT INTO {self.TableName} (Id, Name, Gender, Birthdate, Address) VALUES (?, ?, ?, ?, ?)", user_info)
        self.connection.commit()
        self.connection.close()
