from flask import Blueprint, render_template, redirect, url_for, request
from common.verify import check_admin
from sql.orderitem_query import OrderItem_query

import math

orderitem = Blueprint('orderitem', __name__)

# TODO : 사용성이 좋게 UI에 표시되는걸 변경해주는 건 어떤지?... ex) 주문상품명, 주문정보(주문한사람).. 등등
@orderitem.route('/orderitem')
@check_admin
def orderitem_list():  
    page = request.args.get('page', default=1, type=int) 
    try:
        per_page = 10

        orderitems = OrderItem_query('crm', 'orderitems')
        result_datas = [] # 결과 데이터 삽입용
        datas = orderitems.total_data_query(page, per_page)
        
        # 페이지네이션
        total_data_len = datas['data_length'] # 데이터 전체 갯수
        page_range = math.ceil(total_data_len/per_page) # 페이지 갯수 구하기
        
        # 데이터 자르기
        result_datas = datas['datas']
        
        # 의도치 않은 페이지 이동시 예외처리
        if page < 1:
            page = 1
            return redirect(url_for('orderitem.orderitem_list'))
        elif page > page_range:
            page = page_range
            return redirect(url_for('orderitem.orderitem_list'))

       # 페이지네이션
        start_page = page - (page-1) % 5 # 5개 단위로 끊기
        end_page = min(start_page + 4, page_range) # 끝페이지 정해주기
        
        return render_template('component/orderitem.html',page = page, datas = result_datas, page_range = page_range, start_page = start_page, end_page = end_page)
    
    except TypeError:
        return redirect('orderitem', next='/1')