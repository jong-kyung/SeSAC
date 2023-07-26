import jwt
import os
import datetime # 토큰 저장시 사용하기 위한 라이브러리 
import hashlib
import jwt # JWT 토큰 생성용 라이브러리
import uuid
from flask import Flask, url_for, redirect, render_template, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'SESAC'

app=Flask(__name__) 
app.instance_path = os.path.abspath('DB')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db' # 첫 번째 데이터베이스 연결 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 자동동기화 끄기

app.config['SQLALCHEMY_BINDS'] = {
    'auth_db' : 'sqlite:///auth.db'
}

db = SQLAlchemy(app)

from sql.login_query import Login_query
from common.verify import check_admin

# * Router 정의
from routes.user import user
# from routes.store import store
# from routes.item import item
# from routes.order import order
# from routes.orderitem import orderitem
# from routes.kiosk import kiosk

# Blueprint
app.register_blueprint(user) 
# app.register_blueprint(store)
# app.register_blueprint(item)
# app.register_blueprint(order)
# app.register_blueprint(orderitem)
# app.register_blueprint(kiosk)

# ! auth.db
class auth_user(db.Model): # 일반 사용자 테이블 정의
    __bind_key__ = 'auth_db'
    __tablename__ = 'users' # 테이블 이름정의(옵셔널)
    _id = db.Column(db.Integer, primary_key = True)
    Id = db.Column(db.String(100), unique = True, nullable = False)
    Username = db.Column(db.String(120), unique = True, nullable = False)
    Password = db.Column(db.String(120), unique = True, nullable = False)

class admin(db.Model): # 일반 사용자 테이블 정의
    __bind_key__ = 'auth_db'
    _id = db.Column(db.Integer, primary_key = True)
    Id = db.Column(db.String(100), unique = True, nullable = False)
    Username = db.Column(db.String(120), unique = True, nullable = False)
    Password = db.Column(db.String(120), unique = True, nullable = False)

# ! crm.db
class users(db.Model):
    __bind_key__ = 'default'
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    Name = db.Column(db.String(120), nullable = False)
    Gender = db.Column(db.String(100), nullable = False)
    Birthdate = db.Column(db.String(120), nullable = False)
    Address = db.Column(db.String(120), nullable = False)

    orderR = db.relationship('orders', backref='users')


class stores(db.Model):
    __bind_key__ = 'default'
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    Name = db.Column(db.String(120), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Address = db.Column(db.String(120), nullable = False)

    orderR = db.relationship('orders', backref='stores')

class items(db.Model):
    __bind_key__ = 'default'
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    Name = db.Column(db.String(120), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Price = db.Column(db.String(100), nullable = False)

    orderItemR = db.relationship('orderitems', backref='items')


class orders(db.Model):
    __bind_key__ = 'default'
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    OrderAt = db.Column(db.String(32), nullable = False)
    StoreId = db.Column(db.String(32), db.ForeignKey('stores.Id'))
    userId = db.Column(db.String(64), db.ForeignKey('users.Id'))

    orderItemR = db.relationship('orderitems', backref='orders')

class orderitems(db.Model):
    __bind_key__ = 'default'
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    OrderId = db.Column(db.String(32), db.ForeignKey('orders.Id'))
    ItemId = db.Column(db.String(64), db.ForeignKey('items.Id'))

@app.route('/sign', methods=['POST'])
def sign_up():
    # 사용자의 계정
    sign_id = request.form['sign_id']
    sign_pw = request.form['sign_pw']
    
    # 사용자의 정보
    user_id = uuid.uuid4()
    user_name = request.form['user_name']
    user_gender = request.form['user_gender']
    user_birthdate = request.form['user_birthdate']
    user_address = request.form['user_address']

    user_info = (str(user_id), user_name, user_gender, user_birthdate, user_address)

    pw_hash = hashlib.sha256(sign_pw.encode('utf-8')).hexdigest() # 해쉬암호화
    save_data = (str(user_id), sign_id, pw_hash)

    user_request = Login_query(auth_user) # 회원가입시 접근하는 DB

    user_id = user_request.check_overlap(sign_id)
    
    if user_id:
        return jsonify({'result':'fail', 'msg': '이미 존재하는 계정입니다'})
    else:
        user_request.insert_user_id(save_data)

        return redirect('/')
               

@app.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()

    find_user = Login_query(auth_user)
    find_admin = Login_query(admin)

    user_id = find_user.user_auth(id, pw_hash)
    admin_id = find_admin.user_auth(id, pw_hash)
    
    if user_id:
        payload = {
            'id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        response = make_response(redirect(url_for('kiosk.store_ui'))) # 응답객체 생성
        
        response.set_cookie('token', token, httponly=True) # 토큰을 쿠키에 저장
        return response
    
    elif admin_id:
        payload = {
            'id': id,
        }
        
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        response = make_response(redirect(url_for('user.user_list'))) # 응답객체 생성
        
        response.set_cookie('token', token, httponly=True) # 토큰을 쿠키에 저장
        return response
    
    else:
        return jsonify({'result':'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다'})
    

@app.route('/logout')
@check_admin
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('token')
    
    return response


@app.route('/')
def root():
    token = request.cookies.get('token') # 토큰 받아오기
    find_user = Login_query(auth_user)
    find_admin = Login_query(admin)
    
    if token is None:
        return render_template('login.html')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    # TODO 사용자 / test 아이디가 같은경우에 어떻게 처리할 것 인지, 보통 계정용 DB와 crm용 DB를 나누는게 실무에서도 사용하는 방식임
        if find_admin.user_info(payload['id']):
            return redirect(url_for('user.user_list'))
        elif find_user.user_info(payload['id']):
            return redirect(url_for('kiosk.store_ui'))
    except jwt.exceptions.ExpiredSignatureError:
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=8080)