import datetime # 토큰 저장시 사용하기 위한 라이브러리 
import hashlib
import jwt # JWT 토큰 생성용 라이브러리
import uuid

from flask import Blueprint, make_response, redirect, url_for, jsonify, request

from sql.login_query import Login_query
from common.verify import check_admin

SECRET_KEY = 'SESAC'

auth = Blueprint('auth', __name__)

@auth.route('/sign', methods=['POST'])
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
    save_data = (sign_id, pw_hash)

    find_user = Login_query('auth', 'users') # 회원가입시 접근하는 DB
    crm_user = Login_query('crm', 'users') # 사용자의 정보를 저장하는 DB

    user_id = find_user.check_overlap(sign_id)
    
    if user_id:
        return jsonify({'result':'fail', 'msg': '이미 존재하는 계정입니다'})
    else:
        find_user.insert_user_id(save_data)
        crm_user.insert_user_info(user_info)

        return redirect('/')
               

@auth.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()

    find_user = Login_query('auth', 'users')
    find_admin = Login_query('auth', 'admin')

    user_id = find_user.user_auth(id, pw_hash)
    admin_id = find_admin.user_auth(id, pw_hash)
    if user_id:
        payload = {
            'id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        response = make_response(redirect(url_for('kiosk.main_ui'))) # 응답객체 생성
        
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
    
@auth.route('/logout')
@check_admin
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('token')
    return response

