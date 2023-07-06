# 파일명변경하기
import csv
import math
from flask import request    

def parse_data(dataname, pages):
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    sub_data = request.args.get('sub-data', default='', type=str)
    per_page = pages # 내가 보여줄 페이지 갯수
    headers= [] # 맨 위의 헤딩 저장
    datas = [] # 데이터 담을 list
    result_datas = [] # 데이터 쪼개서 보여줄때 넣어주기
        
    with open(f'./crm/{dataname}.csv', 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data) # 첫번째 줄 넣기
        for row in csv_data:
            if search_name in row[1]:
                if sub_data in row[2]:
                    datas.append(row) # csv 데이터 삽입
            
    # TODO : 페이지네이션 함수 따로만들기
    total_len = len(datas) - 1 # header 제외
    total_range = math.floor(total_len // per_page) # 페이지네이션 갯수 
    start_index = (page - 1) * per_page 
    end_index = start_index + per_page

    start_page = ((page - 1) // 5)*5 + 1 # 현재페이지를 5로 나눠 몫을 구한 후 5를 곱하여 5개단위로 끊기
    end_page = min(start_page + 4, total_range) # 전체페이지와 마지막 페이지를 비교하여 더 작은 값 선택
    
    result_datas = datas[start_index:end_index]
    return {
        'headers': headers,
        'result_datas': result_datas,
        'total_range': total_range,
        'page': page,
        'search_name': search_name,
        'sub_data': sub_data,
        'start_page': start_page,
        'end_page': end_page
    }
