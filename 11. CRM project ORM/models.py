from __init__ import db

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
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    Name = db.Column(db.String(120), nullable = False)
    Gender = db.Column(db.String(100), nullable = False)
    Birthdate = db.Column(db.String(120), nullable = False)
    Address = db.Column(db.String(120), nullable = False)

    orderR = db.relationship('orders', backref='users')


class stores(db.Model):
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    Name = db.Column(db.String(120), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Address = db.Column(db.String(120), nullable = False)

    orderR = db.relationship('orders', backref='stores')

class buy_item(db.Model):
    __tablename__ = 'items'
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    Name = db.Column(db.String(120), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Price = db.Column(db.String(100), nullable = False)

    orderItemR = db.relationship('orderitems', backref='items')


class orders(db.Model):
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    OrderAt = db.Column(db.String(32), nullable = False)
    StoreId = db.Column(db.String(32), db.ForeignKey('stores.Id'))
    UserId = db.Column(db.String(64), db.ForeignKey('users.Id'))

    orderItemR = db.relationship('orderitems', backref='orders')

class orderitems(db.Model):
    Id = db.Column(db.String(100), nullable = False, primary_key = True)
    OrderId = db.Column(db.String(32), db.ForeignKey('orders.Id'))
    ItemId = db.Column(db.String(64), db.ForeignKey('items.Id'))