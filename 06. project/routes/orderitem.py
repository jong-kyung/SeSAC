from flask import Blueprint, request, render_template
from common.verify import check_login
from common.sqlite_query import SQLite3_query
import math

orderitem = Blueprint('orderitem', __name__)

@orderitem.route('/orderitem')
# @check_login
def orderitem_list():  
    page = request.args.get('page', default=1, type=int) 
    orderitems = SQLite3_query('orderitems')
    
    headers = orderitems.schema_query() # schema 받아오기
    datas = orderitems.total_data_query() # 데이터들 받아오기
    result_datas = [] # 결과 데이터 삽입용

    # -------- 페이지네이션 --------
    per_page = 15
    total_data_len = len(datas) # 데이터 전체 갯수
    page_range = math.ceil(total_data_len/per_page) # 페이지 갯수 구하기
        # ---- 데이터 자르기 ----
    start_index = (page - 1)*per_page # 데이터를 자르기 위한 인덱싱
    end_index = start_index + per_page
    result_datas = datas[start_index:end_index] # 데이터 자르기

    if page < 1:
        page = 1
    elif page > page_range:
        page = page_range

    start_page =  ((page - 1) // 5)*5 + 1  # 현재페이지를 5로 나눠 몫을 구한 후 5를 곱하여 5개단위로 끊기
    end_page = min(start_page + 4, page_range) 
    # print(f'현재:{page}, 처음:{start_page},마지막:{end_page}')



    return render_template('list.html', dataname='orderitem', page = page, headers = headers, datas = result_datas, page_range = page_range, start_page = start_page, end_page = end_page)


@orderitem.route('/orderitem/<param>')
# @check_login
def orderitem_info(param):
    orderitem = SQLite3_query('orderitems')
    headers = orderitem.schema_query()
    findData = orderitem.detail_info(param)

    return render_template('search_detail.html', headers=headers, datas=findData)
