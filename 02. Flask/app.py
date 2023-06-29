from flask import Flask, url_for, redirect, render_template
import csv

app = Flask(__name__) # 고유식별자를 넣어주어야함 보통 __name__으로 작명함

@app.route('/')
def home():
    with open('./csv/user.csv', 'r') as file:
        csv_reader = csv.reader(file)   
        return render_template('list.html', datas=csv_reader, dataname='user')
    # """ """ 는 자바스크립트에서의 백틱과 유사함.

@app.route('/user')
def user_none():
    return """
    <ul>
    <li><a href='/user/tom'>tom</a></li>
    <li><a href='/user/john'>john</a></li>
    <li><a href='/user/bill'>bill</a></li>
    """

@app.route('/user/<param>')
def user_info(param):
    findData = []
    with open('./csv/user.csv', 'r', newline='') as file:
        csv_file = csv.reader(file)
        findData.append(next(csv_file)) # 첫번째 줄 넣기
        for row in csv_file:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)

@app.route('/store')
def store():
        with open('./csv/store.csv', 'r') as file:
            csv_reader = csv.reader(file)   
            return render_template('list.html', datas=csv_reader, dataname='store')

@app.route('/store/<param>')
def store_info(param):
    findData = []
    with open('./csv/store.csv', 'r', newline='') as file:
        csv_file = csv.reader(file)
        findData.append(next(csv_file)) # 첫번째 줄 넣기
        for row in csv_file:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)
            
@app.route('/item')
def item():
        with open('./csv/item.csv', 'r') as file:
            csv_reader = csv.reader(file)   
            return render_template('list.html', datas=csv_reader, dataname='item')
        
@app.route('/item/<param>')
def item_info(param):
    findData = []
    with open('./csv/item.csv', 'r', newline='') as file:
        csv_file = csv.reader(file)
        findData.append(next(csv_file)) # 첫번째 줄 넣기
        for row in csv_file:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)    
            
@app.route('/admin')
def admin():
    return redirect(url_for('user', name='admin'))

if __name__ == '__main__':
    app.run(debug=True, port=8080) # 기본로컬주소 :127.0.0.1:5000
