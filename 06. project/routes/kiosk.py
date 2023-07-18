from flask import Blueprint, render_template, redirect, url_for, make_response, request

import math

from common.verify import check_user
from sql.store_query import Store_query
from sql.item_query import Item_query
from sql.order_query import Order_query
from sql.orderitem_query import OrderItem_query

kiosk = Blueprint('kiosk', __name__)

@kiosk.route('/kiosk')
@check_user
def store_ui():
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    sub_data = request.args.get('sub_data', default='', type=str)
    current_url = request.path
    print(current_url)
    try:
        per_page = 12
  
        stores = Store_query('crm', 'stores')
        headers = stores.schema_query() # schema 받아오기
        store_types = stores.find_data_query('Type') # Type 받아오기
        result_datas = [] # 결과 데이터 삽입용
        datas = stores.total_data_query(page, per_page, 'Name', search_name, 'Type', sub_data)

        # -------- 페이지네이션 --------
        total_data_len = datas['data_length'] # 데이터 전체 갯수
        page_range = math.ceil(total_data_len/per_page) # 페이지 갯수 구하기
            # ---- 데이터 자르기 ----
        result_datas = datas['datas'] # 데이터 자르기
        
        # 의도치 않은 페이지 이동시 예외처리
        if page < 1:
            page = 1
            return redirect(url_for('kiosk.store_ui'))
        elif page > page_range:
            page = page_range
            return redirect(url_for('kiosk.store_ui'))

       # 페이지네이션
        start_page = page - (page-1) % 5 # 5개 단위로 끊기
        end_page = min(start_page + 4, page_range) # 끝페이지 정해주기

        return render_template('kiosk/kiosk_list.html', search_name = search_name, sub_data = sub_data, page = page, types = store_types, headers = headers, datas = result_datas, page_range = page_range, start_page = start_page, end_page = end_page, current_url = current_url)
    
    except TypeError:
        return redirect('kiosk', next='/1')
    
@kiosk.route('/kiosk/<store_id>')
@check_user
def item_ui(store_id):
    page = request.args.get('page', default=1, type=int) 
    search_name = request.args.get('name', default='', type=str)
    sub_data = request.args.get('sub_data', default='', type=str)
    current_url = request.path

    try:
        per_page = 9

        items = Item_query('crm', 'items')
        headers = items.schema_query() # schema 받아오기
        item_types = items.find_data_query('Type') # Type 받아오기
        result_datas = [] # 결과 데이터 삽입용
        datas = items.total_data_query(page, per_page, 'Name', search_name, 'Type', sub_data)

        # -------- 페이지네이션 --------
        total_data_len = datas['data_length'] # 데이터 전체 갯수
        page_range = math.ceil(total_data_len/per_page) # 페이지 갯수 구하기
            # ---- 데이터 자르기 ----
        result_datas = datas['datas'] # 데이터 자르기
        
        # 의도치 않은 페이지 이동시 예외처리
        if page < 1:
            page = 1
            return redirect(url_for('kiosk.item_ui'))
        elif page > page_range:
            page = page_range
            return redirect(url_for('kiosk.item_ui'))

    # 페이지네이션
        start_page = page - (page-1) % 5 # 5개 단위로 끊기
        end_page = min(start_page + 4, page_range) # 끝페이지 정해주기
        
        return render_template('kiosk/kiosk_list.html', search_name = search_name, sub_data = sub_data, page = page, types = item_types, headers = headers, datas = result_datas, page_range = page_range, start_page = start_page, end_page = end_page, current_url = current_url)
        
    except TypeError:
        return redirect('kiosk', next='/1')

@kiosk.route('/kiosk/<store_id>/<item_id>')
@check_user
def kiosk_result(store_id, item_id):
    return print('hi')

@kiosk.route('/kiosk/logout')
@check_user
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('token')
    
    return response

