from flask import Blueprint, request, render_template
import csv
from common.pagination import parse_data
from common.verify import check_login
order = Blueprint('order', __name__)


@order.route('/order')
@check_login
def order_list():
    data = parse_data('order', 10)

    return render_template('list.html', dataname='order', headers = data['headers'], datas = data['result_datas'], total_range = data['total_range'], page = data['page'], search_name = data['search_name'], sub_data=data['sub_data'], start_page = data['start_page'], end_page = data['end_page'])
    
@order.route('/order/<param>')
@check_login
def order_info(param):
    findData = []
    with open('./crm/order.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data))
        for row in csv_data:
            if param in row:
                findData.append(row)
    return render_template('detail.html', datas=findData) 
                
