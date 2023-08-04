from flask import Flask, render_template, request
from database import Database
import json

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_post():
    title = request.form['title']
    message = request.form['message']
    sql = 'INSERT INTO board (title, message) VALUES ("{}", "{}")'.format(title, message)
    db.execute(sql)
    db.commit()
    return 'OK'

@app.route('/list', methods=['get'])
def list_post():
    sql = 'SELECT * FROM board'
    result = db.execute_fetch(sql)
    tuple_keys = ('id', 'title', 'message')
    dict_list = []
    for r in result:
        dict_value = dict(zip(tuple_keys, r))
        dict_list.append(dict_value)

    return result

@app.route('/delete', methods=['POST'])
def delete_post():
    id = request.form['id']
    sql = f'DELETE FROM board WHERE id = {id}'
    db.execute(sql)
    db.commit()
    return 'DEL'

@app.route('/edit', methods=['POST'])
def edit_post():
    id = request.form['id']
    title = request.form['title']
    message = request.form['message']
    sql = f'UPDATE board SET title = "{title}", message = "{message}" WHERE id = {id}'
    db.execute(sql)
    db.commit()
    return 'hi'
if __name__ == '__main__':
    app.run(port=8080, debug=True)