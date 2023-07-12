from flask import Flask, render_template
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
    # TODO : 월간 매출액 합산을 구하시오
    
    return render_template('index.html', rows=rows)

if __name__ == 'main':
    app.run(debug=True, port=8080)