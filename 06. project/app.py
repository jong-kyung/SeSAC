import datetime # 토큰 저장시 사용하기 위한 라이브러리 / 목적적어주기
import hashlib # 해쉬암호화 라이브러리
import jwt # JWT 토큰 생성용 라이브러리

from flask import Flask, url_for, redirect, render_template, request, jsonify, make_response

from common.sqlite_query import SQLite3_query
from routes.user import user
from routes.store import store
from routes.item import item
from routes.order import order
from routes.orderitem import orderitem
from common.verify import check_login

SECRET_KEY = 'SESAC'

app=Flask(__name__) 
app.register_blueprint(user) 
app.register_blueprint(store)
app.register_blueprint(item)
app.register_blueprint(order)
app.register_blueprint(orderitem)

# TODO : 만약 주소창에 -1을 입력할경우엔 어떻게 할것인지?
# @app.route('/sign', methods=['POST'])
# def sign_up():
#     sign_id = request.form['sign_id']
#     sign_pw = request.form['sign_pw']

#     pw_hash = hashlib.sha256(sign_pw.encode('utf-8')).hexdigest() # 해쉬암호화

#     save_data = [sign_id, pw_hash]

#     with open('./crm/login.csv', 'r') as file:
#             csv_file = csv.reader(file)
#             exists = False
#             for data in  csv_file:
#                 if sign_id in data:
#                     exists = True
#                     break
#             if not exists:
#                 with open('./crm/login.csv', 'a', newline='') as datas:
#                     csv_data = csv.writer(datas)
#                     csv_data.writerow(save_data)
#             else:
#                 return jsonify({'result':'fail', 'msg': '이미 존재하는 계정입니다'})

#     return redirect('/')

# @app.route('/login', methods=['POST'])
# def login():
#     id = request.form['id']
#     pw = request.form['pw']
#     pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
#     result = []

#     with open('./crm/login.csv', 'r') as file:
#         csv_data = csv.reader(file)
#         for row in csv_data:
#             if row[0] == id and row[1] == pw_hash:
#                 result.append(row)
#                 break
    
#     # TODO : len으로 작성하면 보안에 취약할 것 같은데 어떻게 개선하면 좋을지? / 보통 실무에서도 이렇게 한다고함.
#     if len(result) == 1:
#         payload = {
#             'id': id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*30)
#         }
#         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#         response = make_response(redirect(url_for('user.user_list'))) # 응답객체 생성
        
#         response.set_cookie('token', token, httponly=True) # 토큰을 쿠키에 저장
#         return response
#     else:
#         return jsonify({'result':'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다'})
    
# @app.route('/logout')
# @check_login
# def logout():
#     response = make_response(redirect('/'))
#     response.delete_cookie('token')
#     return response

# @app.route('/')
# def root():
#     token = request.cookies.get('token') # 토큰 받아오기
    
#     if token is None:
#         return render_template('login.html')
#     try:
#         jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         return redirect(url_for('user.user_list'))
#     except jwt.exceptions.ExpiredSignatureError:
#         return render_template('login.html')
    
#     # 고른이유가 뭔지 설명할 수 있어야함

@app.route('/')
def index():
    return redirect(url_for('user.user_list'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)