from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.instance_path = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db' # DB연결
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 자동동기화 끄기
app.debug = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users' # 테이블 이름정의(옵셔널)
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))
    # 관계 셋업
    orderR = db.relationship('Order', backref='users')

    def __repr__(self): # Class가 출력(print)되는 방식 정의
        return f'<User {self.name}, {self.gender}, {self.birthdate}>'

class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    address = db.Column(db.String(64))

    orderR = db.relationship('Order', backref='stores')

    def __repr__(self):
        return f'<Store {self.name}, {self.type}>'

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(64), primary_key = True)
    orderAt = db.Column(db.String(32))
    StoreId = db.Column(db.String(32), db.ForeignKey('stores.id'))
    userId = db.Column(db.String(64), db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Order {self.id}, {self.orderAt}>'

@app.route('/')
def home():
    # users = User.query.filter_by(name = '양민재').all()
    # print(users)
    
    # stores = Store.query.all()
    # for s in stores:
    #     print(s)
    
    # orders = Order.query.all()
    # print(orders)
    
    # users = User.query.filter_by(name = '양민재').first()
    # order_by_user = users.orderR
    # print(order_by_user)
    
    # ? 윤수빈이 방문한 매장 찾기
    # ! join 방식
    # result = db.session.query(Store.name).join(Order, Store.id == Order.StoreId).join(User, Order.userId == User.id).filter(User.name == '양민재').all()
    # print(result)

    # ! backref 이용
    users = User.query.filter_by(name="윤수빈").first()
    order_by_user = users.orderR
    print(order_by_user)
    
    # 윤수빈이 주문한 주문내역
    for order in order_by_user:
        store = order.stores # join하는것
        print(f"윤수빈이 방문한 상점은 {store.name} 시간은 {order.orderAt}")


    # ! SQL 쿼리문
    # ? SELECT stores.name FROM stores JOIN orders IN stores.id = orders.storeId JOIN users IN orders.userId = users.id
    return 'Hello'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=8080)