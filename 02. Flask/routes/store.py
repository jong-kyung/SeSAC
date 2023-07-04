from flask import Blueprint, request, render_template
import csv
import math
from common.verify import check_login
store = Blueprint('store', __name__)

@store.route('/store')
@check_login
def store_list():
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

@store.route('/store/<param>')
@check_login
def store_info(param):
    findData = []
    with open('./crm/store.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)
            