from flask import Flask, redirect, request
from functools import wraps
from common.sqlite_query import SQLite3_query

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
            find_user = SQLite3_query('user')
            user_id = find_user.user_auth(payload['id'])
            
            if len(user_id) == 1:
                return  (f(*args, **kwargs))
        
        except jwt.DecodeError:
            pass
    
    return decorated_function