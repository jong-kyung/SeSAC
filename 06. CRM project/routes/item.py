from flask import Blueprint, render_template, redirect, url_for, request
from common.verify import check_admin
from sql.item_query import Item_query

import math

item = Blueprint('item', __name__)

@item.route('/item')
@check_admin
def item_list():  
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    sub_data = request.args.get('sub_data', default='', type=str)
    try:
        per_page = 10

        items = Item_query('crm', 'items')
        item_types = items.find_data_query('Type') # Type 받아오기
        result_datas = [] # 결과 데이터 삽입용
        datas = items.total_data_query(page, per_page, 'Name', search_name, 'Type', sub_data)

        # 페이지네이션
        total_data_len = datas['data_length'] # 데이터 전체 갯수
        page_range = math.ceil(total_data_len/per_page) # 페이지 갯수 구하기
        
        # 데이터 자르기
        result_datas = datas['datas']
        
        # 의도치 않은 페이지 이동시 예외처리
        if page < 1:
            page = 1
            return redirect(url_for('item.item_list'))
        elif page > page_range:
            page = page_range
            return redirect(url_for('item.item_list'))

       # 페이지네이션
        start_page = page - (page-1) % 5 # 5개 단위로 끊기
        end_page = min(start_page + 4, page_range) # 끝페이지 정해주기
        
        return render_template('component/item.html', search_name = search_name, sub_data = sub_data, page = page, types = item_types, datas = result_datas, page_range = page_range, start_page = start_page, end_page = end_page)
    
    except TypeError:
        return redirect('item', next='/1')
        


@item.route('/item/<param>')
@check_admin
def item_info(param):
    item = Item_query('crm', 'items')
    findData = item.detail_info(param)

    return render_template('./component/item_detail.html', datas=findData)
