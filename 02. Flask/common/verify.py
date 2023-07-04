from flask import Flask, redirect, request
from functools import wraps
import csv
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

            with open('./crm/login.csv', 'r') as file:
                csv_data = csv.reader(file)
                for row in csv_data:
                    if row[0] == payload['id']:
                        return  (f(*args, **kwargs))
        
        except jwt.DecodeError:
            pass
    
    return decorated_function