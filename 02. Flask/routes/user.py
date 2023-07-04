from flask import Blueprint, request, render_template
import csv
import math
from common.verify import check_login
user = Blueprint('user', __name__)

# 연산은 백엔드에서 처리하는게 가장 좋음, 연산이 적은거는 프론트에서
@user.route('/user')
@check_login
def user_list():
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

            start_page = ((page - 1) // 5)*5 + 1 # 현재페이지를 5로 나눠 몫을 구한 후 5를 곱하여 5개단위로 끊기
            end_page = min(start_page + 4, total_range) # 전체페이지와 마지막 페이지를 비교하여 더 작은 값 선택
            
            result_datas = datas[start_index:end_index]

            return render_template('list.html', dataname='user', headers = headers, datas = result_datas, total_range = total_range, page = page, search_name = search_name, gender=gender, start_page = start_page, end_page = end_page)
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
