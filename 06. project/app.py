import jwt
from flask import Flask, url_for, redirect, render_template, request

# * SQL 쿼리 접근
from sql.login_query import Login_query

# * Router 정의
from routes.auth import auth
from routes.user import user
from routes.store import store
from routes.item import item
from routes.order import order
from routes.orderitem import orderitem
from routes.kiosk import kiosk

SECRET_KEY = 'SESAC'

app=Flask(__name__) 

app.register_blueprint(auth)
app.register_blueprint(user) 
app.register_blueprint(store)
app.register_blueprint(item)
app.register_blueprint(order)
app.register_blueprint(orderitem)
app.register_blueprint(kiosk)

@app.route('/')
def root():
    token = request.cookies.get('token') # 토큰 받아오기
    find_user = Login_query('auth', 'users')
    find_admin = Login_query('auth', 'admin')
    
    if token is None:
        return render_template('login.html')
    try:
        payload =jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        if find_admin.user_info(payload['id']):
            return redirect(url_for('user.user_list'))
        elif find_user.user_info(payload['id']):
            return redirect(url_for('kiosk.store_ui'))
    except jwt.exceptions.ExpiredSignatureError:
        return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)