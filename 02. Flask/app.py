from flask import Flask, url_for, redirect, render_template, request, jsonify, make_response
import csv
import math
import datetime 
import jwt # JWT 토큰 생성용 라이브러리
import hashlib # 해쉬암호화 라이브러리
SECRET_KEY = 'SESAC'

app = Flask(__name__) # 고유식별자를 넣어주어야함 보통 __name__으로 작명함

@app.route('/sign', methods=['POST'])
def sign_up():
    sign_id = request.form['sign_id']
    sign_pw = request.form['sign_pw']

    pw_hash = hashlib.sha256(sign_pw.encode('utf-8')).hexdigest() # 해쉬암호화

    save_data = {'id': sign_id,'pw': pw_hash}
    with open('./crm/login.csv', 'w') as file:
        csv_data = csv.writer(file)
        for key, value in save_data.items():
            csv_data.writerow([key, value])
    
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    result = []

    with open('./crm/login.csv', 'r') as file:
        csv_data = csv.reader(file)
        for row in csv_data:
            if row[1] == id:
                result.append(row[1])
                continue
            if row[1] == pw_hash:
                result.append(row[1])
    if result != []:
        payload = {
            'id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        response = make_response(redirect(url_for('user'))) # 응답객체 생성
        
        response.set_cookie('token', token, httponly=True) # 토큰을 쿠키에 저장
        return response
    else:
        return jsonify({'result':'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다'})

@app.route('/')
def root():
        return render_template('login.html')

# 연산은 백엔드에서 처리하는게 가장 좋음, 연산이 적은거는 프론트에서
@app.route('/user')
def user():
    token = request.cookies.get('token') # 토큰 받아오기
    try: 
        page = request.args.get('page', default=1, type=int) 
        search_name = request.args.get('name', default='', type=str)
        gender = request.args.get('sub-data', default='', type=str)
        
        per_page = 35 # 내가 보여줄 페이지 갯수
        headers= [] # 맨 위의 헤딩 저장
        datas = [] # 데이터 담을 list
        result_datas = [] # 데이터 쪼개서 보여줄때 넣어주기
        filter_datas = []
        
        with open('./crm/user.csv', 'r') as file:
            csv_data = csv.reader(file)
            headers = next(csv_data) # 첫번째 줄 넣기
            for row in csv_data:
                if search_name in row[1]:
                    datas.append(row) # csv 데이터 삽입

            for data in datas: # 데이터들을 for문을 통해 필터링 작업
                if gender in data:
                    filter_datas.append(data) 
                    datas = filter_datas
                
            total_len = len(datas) - 1 # header 제외
            total_range = math.ceil(total_len // per_page) # 페이지네이션 갯수
            start_index = (page - 1) * per_page 
            end_index = start_index + per_page

            start_page = ((page - 1) // 5)*5 + 1 # 5개 단위로 끊기
            end_page = min(start_page + 4, total_range) # 전체페이지와 마지막 페이지를 비교하여 더 작은 값 선택
            
            result_datas = datas[start_index:end_index]

            return render_template('list.html', dataname='user', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name, gender=gender, start_page = start_page, end_page = end_page)
        # """ """ 는 자바스크립트에서의 백틱과 유사함.
    except jwt.ExpiredSignatureError:
        return '토큰이 만료되었습니다'
    except jwt.InvalidTokenError:
        return '유효하지 않은 토큰입니다'

@app.route('/user/<param>')
def user_info(param):
    findData = []
    with open('./crm/user.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)

@app.route('/store')
def store():
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    store_type = request.args.get('sub-data', default='', type=str)

    per_page = 35 
    headers= [] 
    datas = [] 
    result_datas = [] 
    filter_datas = []
    
    with open('./crm/store.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) 
        for row in csv_data:
            if search_name in row[1]:
                datas.append(row)
           
        for data in datas: 
            if store_type in data:
                filter_datas.append(data) 
                datas = filter_datas
                
        total_len = len(datas) - 1 
        total_range = math.ceil(total_len // per_page) 
        start_index = (page - 1) * per_page 
        end_index = start_index + per_page

        start_page = ((page - 1) // 5)*5 + 1 #
        end_page = min(start_page + 4, total_range) 
        
        result_datas = datas[start_index:end_index]
        
        return render_template('list.html', dataname='store', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name, start_page = start_page, end_page = end_page)

@app.route('/store/<param>')
def store_info(param):
    findData = []
    with open('./crm/store.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)
            
@app.route('/item')
def item():
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    item_type = request.args.get('sub-data', default='', type=str)

    per_page = 35 
    headers= [] 
    datas = [] 
    result_datas = [] 
    filter_datas = []
    
    with open('./crm/item.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) 
        for row in csv_data:
            if search_name in row[1]:
                datas.append(row)
        
        for data in datas: 
            if item_type in data:
                filter_datas.append(data) 
                datas = filter_datas

        total_len = len(datas) - 1 
        total_range = math.ceil(total_len // per_page) 
        start_index = (page - 1) * per_page 
        end_index = start_index + per_page

        start_page = ((page - 1) // 5)*5 + 1 #
        end_page = min(start_page + 4, total_range) 
        
        result_datas = datas[start_index:end_index]
        
        return render_template('list.html', dataname='item', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name, start_page = start_page, end_page = end_page)
    
@app.route('/item/<param>')
def item_info(param):
    findData = []
    with open('./crm/item.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)    
            
@app.route('/order')
def order():
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    
    per_page = 35
    headers= []
    datas = []
    result_datas = []
    
    with open('./crm/order.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            if search_name in row[1]:
                datas.append(row)
                   
        total_len = len(datas) - 1 
        total_range = math.ceil(total_len // per_page) 
        start_index = (page - 1) * per_page 
        end_index = start_index + per_page

        start_page = ((page - 1) // 5)*5 + 1 #
        end_page = min(start_page + 4, total_range) 
        
        result_datas = datas[start_index:end_index]
        
        return render_template('list.html', dataname='order', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name, start_page = start_page, end_page = end_page)
    
@app.route('/order/<param>')
def order_info(param):
    findData = []
    with open('./crm/order.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data))
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData) 
                   
@app.route('/ordereditem')
def ordereditem(page=1):
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    
    per_page = 35
    headers= []
    datas = []
    result_datas = []
    
    with open('./crm/orderitem.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            if search_name in row[1]:
                datas.append(row)
                
        total_len = len(datas) - 1 
        total_range = math.ceil(total_len // per_page) 
        start_index = (page - 1) * per_page 
        end_index = start_index + per_page

        start_page = ((page - 1) // 5)*5 + 1 
        end_page = min(start_page + 4, total_range) 
        
        result_datas = datas[start_index:end_index]
        
        return render_template('list.html', dataname='ordereditem', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name, start_page = start_page, end_page = end_page)
    
@app.route('/ordereditem/<param>')
def orderitem_info(param):
    findData = []
    with open('./crm/orderitem.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData) 
                   

if __name__ == '__main__':
    app.run(debug=True, port=8080) # 기본로컬주소 :127.0.0.1:5000
