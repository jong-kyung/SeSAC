from flask import Flask, url_for, redirect, render_template
import csv

app = Flask(__name__) # 고유식별자를 넣어주어야함 보통 __name__으로 작명함

@app.route('/')
def home():
    with open('./csv/user.csv', 'r') as file:
        csv_reader = csv.reader(file)   
        return render_template('index.html', username=csv_reader)
    # """ """ 는 자바스크립트에서의 백틱과 유사함.

@app.route('/user')
def user_none():
    return """
    <ul>
    <li><a href='/user/tom'>tom</a></li>
    <li><a href='/user/john'>john</a></li>
    <li><a href='/user/bill'>bill</a></li>
    """


@app.route('/<id>')
def user(id):
     with open('./csv/user.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if id in row:
                return render_template('user.html', finduser=row)

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/admin')
def admin():
    return redirect(url_for('user', name='admin'))

if __name__ == '__main__':
    app.run(debug=True, port=8080) # 기본로컬주소 :127.0.0.1:5000
