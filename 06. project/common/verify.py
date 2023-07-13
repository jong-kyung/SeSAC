from flask import Flask, redirect, request
from functools import wraps
import sqlite3

import jwt # JWT 토큰 생성용 라이브러리
SECRET_KEY = 'SESAC'

# 로그인여부 확인하는 데코레이터 함수
def check_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token') # 토큰 받아오기

        if token is None:
            return redirect('/')
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            conn = sqlite3.connect('./DB/crm.db')
            cursor = conn.cursor()

            cursor.execute("SELECT Id FROM user WHERE username = ?", payload['id'])
            user_id = cursor.fetchone()
            
            if len(user_id) == 1:
                return  (f(*args, **kwargs))
        
        except jwt.DecodeError:
            pass
    
    return decorated_function