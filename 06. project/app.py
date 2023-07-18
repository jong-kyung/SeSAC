import jwt
from flask import Flask, url_for, redirect, render_template, request

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
    
    if token is None:
        return render_template('login.html')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return redirect(url_for('user.user_list'))
    except jwt.exceptions.ExpiredSignatureError:
        return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)