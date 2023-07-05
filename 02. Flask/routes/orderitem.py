from flask import Blueprint, request, render_template
import csv
from common.functions import parse_data
from common.verify import check_login
orderitem = Blueprint('orderitem', __name__)

@orderitem.route('/ordereditem')
@check_login
def orderitem_list():
    data = parse_data('orderitem', 10)

    return render_template('list.html', dataname='orderitem', headers = data['headers'], datas = data['result_datas'], total_range = data['total_range'], page = data['page'], search_name = data['search_name'], gender=data['sub_data'], start_page = data['start_page'], end_page = data['end_page'])
    
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