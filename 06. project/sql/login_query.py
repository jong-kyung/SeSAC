import sqlite3
from sql.sqlite_connect import SQLite3_connect

class Login_query(SQLite3_connect):
    def check_overlap(self, param):
        self.cursor.execute(f"SELECT Id FROM {self.TableName} WHERE username = ?", (param, ))
        user_id = self.cursor.fetchone()
        self.conn.close()

        return user_id
    
    def insert_user(self, param):
        self.cursor.execute(f"INSERT INTO {self.TableName}(UserName, Password) VALUES (?, ?)", param)
        self.conn.commit()
        self.conn.close()

    def user_auth(self, id, pw):
        self.cursor.execute(f"SELECT UserName, Password FROM {self.TableName} WHERE UserName = ? AND Password = ?", (id, pw))
        result = self.cursor.fetchone()
        self.conn.close()


        return result