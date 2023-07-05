from flask import Blueprint, request, render_template
import csv
from common.functions import parse_data
from common.verify import check_login
item = Blueprint('item', __name__)

@item.route('/item')
@check_login
def item_list():
    data = parse_data('item', 10)

    return render_template('list.html', dataname='item', headers = data['headers'], datas = data['result_datas'], total_range = data['total_range'], page = data['page'], search_name = data['search_name'], sub_data=data['sub_data'], start_page = data['start_page'], end_page = data['end_page'])
    
@item.route('/item/<param>')
@check_login
def item_info(param):
    findData = []
    with open('./crm/item.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
    return render_template('detail.html', datas=findData)    
            