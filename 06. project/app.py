from flask import Flask, render_template
import sqlite3

app=Flask(__name__) 

@app.route('/user')
def index():
    header = []
    conn = sqlite3.connect('./DB/crm.db')

    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('users')")
    schemas = cursor.fetchall()
    for schema in schemas:  
        header.append(schema[1])
    print(f'내가 찾는것 :{header}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)