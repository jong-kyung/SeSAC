from flask import Blueprint, request, render_template
import csv
from common.functions import parse_data
from common.verify import check_login
store = Blueprint('store', __name__)

@store.route('/store')
@check_login
def store_list():
    data = parse_data('store', 10)

    return render_template('list.html', dataname='store', headers = data['headers'], datas = data['result_datas'], total_range = data['total_range'], page = data['page'], search_name = data['search_name'], sub_data=data['sub_data'], start_page = data['start_page'], end_page = data['end_page'])

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
            