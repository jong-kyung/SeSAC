from flask import Blueprint, request, render_template
import csv
import math
from common.verify import check_login
orderitem = Blueprint('orderitem', __name__)

@orderitem.route('/ordereditem')
@check_login
def orderitem_list():
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
    
@orderitem.route('/ordereditem/<param>')
@check_login
def orderitem_info(param):
    findData = []
    with open('./crm/orderitem.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
                return render_template('detail.html', datas=findData)