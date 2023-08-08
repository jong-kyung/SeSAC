from flask import Flask, render_template, request
import sqlite3

# DB 
conn = sqlite3.connect('movie_data.db', check_same_thread=False)
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM movies")
    datas = cursor.fetchall()
    return render_template('index.html', datas = datas)


if __name__ == "__main__":
    app.run(port=8080, debug=True)