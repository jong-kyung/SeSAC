from flask import Blueprint, request, render_template
import csv
from common.pagination import parse_data
from common.verify import check_login
user = Blueprint('user', __name__)

# 연산은 백엔드에서 처리하는게 가장 좋음, 연산이 적은거는 프론트에서
@user.route('/user')
@check_login
def user_list():  
    data = parse_data('user', 30)

    return render_template('list.html', dataname='user', headers = data['headers'], datas = data['result_datas'], total_range = data['total_range'], page = data['page'], search_name = data['search_name'], sub_data=data['sub_data'], start_page = data['start_page'], end_page = data['end_page'])
        # """ """ 는 자바스크립트에서의 백틱과 유사함.


@user.route('/user/<param>')
@check_login
def user_info(param):
    findData = []
    with open('./crm/user.csv', 'r', newline='') as file:
        csv_data = csv.reader(file)
        findData.append(next(csv_data)) # 첫번째 줄 넣기
        for row in csv_data:
            if param in row:
                findData.append(row)
    return render_template('detail.html', datas=findData)
