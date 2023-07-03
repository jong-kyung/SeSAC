from flask import Flask, url_for, redirect, render_template, request
import csv
import math

app = Flask(__name__) # 고유식별자를 넣어주어야함 보통 __name__으로 작명함

@app.route('/')
def root():
    return redirect(url_for('user'))

# 연산은 백엔드에서 처리하는게 가장 좋음, 연산이 적은거는 프론트에서
@app.route('/user')
def user():
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
            # TODO : 어떻게 코드를 합칠 수 있을까? 따로하면 작성은 됨..
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
