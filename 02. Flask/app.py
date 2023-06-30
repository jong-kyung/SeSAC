from flask import Flask, url_for, redirect, render_template, request
import csv

app = Flask(__name__) # 고유식별자를 넣어주어야함 보통 __name__으로 작명함

# 연산은 백엔드에서 처리하는게 가장 좋음, 연산이 적은거는 프론트에서
@app.route('/')
def home(page=1):
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    
    per_page = 35
    headers= []
    datas = []
    result_datas = []
    
    with open('./crm/user.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            if search_name in row[1]:
                datas.append(row)
                
        total_len = len(datas) - 1 # header 제외
        total_range = (total_len // per_page) + 1

        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        result_datas = datas[start_index:end_index]
    
        return render_template('list.html', dataname='user', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name)
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
def store(page=1):
    headers= []
    datas = []
    result_datas = []
    per_page = 35
    
    with open('./crm/store.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            datas.append(row)

        total_len = len(datas) - 1 # header 제외
        total_range = (total_len // per_page) + 1

        start_index = per_page*(int(page) - 1)
        end_index = start_index + per_page
        result_datas = datas[start_index:end_index]

        return render_template('list.html', dataname='store', headers=headers, datas=result_datas, total_range = total_range, page=int(page))

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
def item(page=1):
    headers= []
    datas = []
    result_datas = []
    per_page = 35
    
    with open('./crm/item.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            datas.append(row)

        total_len = len(datas) - 1 # header 제외
        total_range = (total_len // per_page) + 1

        start_index = per_page*(int(page) - 1)
        end_index = start_index + per_page
        result_datas = datas[start_index:end_index]

        return render_template('list.html', dataname='item', headers=headers, datas=result_datas, total_range = total_range, page=int(page))
    
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
def order(page=1):
    headers= []
    datas = []
    result_datas = []
    per_page = 35
    
    with open('./crm/order.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            datas.append(row)

        total_len = len(datas) - 1 # header 제외
        total_range = (total_len // per_page) + 1

        start_index = per_page*(int(page) - 1)
        end_index = start_index + per_page
        result_datas = datas[start_index:end_index]

        return render_template('list.html', dataname='order', headers=headers, datas=result_datas, total_range = total_range, page=int(page))
    
@app.route('/order/<param>')
def order_info(param):
    findData = []
    with open('./crm/order.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData) 
                   
@app.route('/ordereditem')
def ordereditem(page=1):
    headers= []
    datas = []
    result_datas = []
    per_page = 35
    
    with open('./crm/orderitem.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            datas.append(row)

        total_len = len(datas) - 1 # header 제외
        total_range = (total_len // per_page) + 1

        start_index = per_page*(int(page) - 1)
        end_index = start_index + per_page
        result_datas = datas[start_index:end_index]

        return render_template('list.html', dataname='ordereditem', headers=headers, datas=result_datas, total_range = total_range, page=int(page))
    
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
