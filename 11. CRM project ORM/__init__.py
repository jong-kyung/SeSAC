import os
from flask import Flask
from models import db 

app=Flask(__name__) 
app.instance_path = os.path.abspath('DB')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db' # 첫 번째 데이터베이스 연결 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 자동동기화 끄기

app.config['SQLALCHEMY_BINDS'] = {
    'auth_db' : 'sqlite:///auth.db'
}

db.init_app(app) # SQLALCHEMY DB를 초기화 하는 방법

# * Router 정의
from routes.auth import auth
from routes.main import main
from routes.user import user
from routes.store import store
from routes.item import item
from routes.order import order
from routes.orderitem import orderitem
# from routes.kiosk import kiosk

# Blueprint
app.register_blueprint(auth) 
app.register_blueprint(main) 
app.register_blueprint(user) 
app.register_blueprint(store)
app.register_blueprint(item)
app.register_blueprint(order)
app.register_blueprint(orderitem)
# app.register_blueprint(kiosk)
    