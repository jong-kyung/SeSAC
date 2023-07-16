import datetime # 토큰 저장시 사용하기 위한 라이브러리 
import hashlib
import jwt # JWT 토큰 생성용 라이브러리

from flask import Blueprint, make_response, redirect, url_for, jsonify, request
from sql.login_query import Login_query
from common.verify import check_login

SECRET_KEY = 'SESAC'

auth = Blueprint('auth', __name__)


@auth.route('/sign', methods=['POST'])
def sign_up():
    sign_id = request.form['sign_id']
    sign_pw = request.form['sign_pw']

    pw_hash = hashlib.sha256(sign_pw.encode('utf-8')).hexdigest() # 해쉬암호화

    save_data = (sign_id, pw_hash)
    find_user = Login_query('auth', 'user')
    user_id = find_user.check_overlap(sign_id)
    
    if user_id:
        return jsonify({'result':'fail', 'msg': '이미 존재하는 계정입니다'})
    else:
        find_user.insert_user(save_data)
        return redirect('/')
               

@auth.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()

    find_user = Login_query('auth', 'user')
    user_id = find_user.user_auth(id, pw_hash)
    if user_id:
        payload = {
            'id': id,
            # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        response = make_response(redirect(url_for('user.user_list'))) # 응답객체 생성
        
        response.set_cookie('token', token, httponly=True) # 토큰을 쿠키에 저장
        return response
    else:
        return jsonify({'result':'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다'})
    
@auth.route('/logout')
@check_login
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('token')
    return response

