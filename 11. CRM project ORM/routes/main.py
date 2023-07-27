import jwt
from flask import Blueprint, render_template, redirect, url_for, request
from sql.login_query import Login_query
from sql.login_query import Login_query
from common.verify import check_admin
from models import auth_user, admin

SECRET_KEY = 'SESAC'

main = Blueprint('main', __name__)

@main.route('/')
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