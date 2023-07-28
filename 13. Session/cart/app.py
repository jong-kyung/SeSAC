from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'abcd1234' # 세션 암호화를 위한 나만의키

#상품 정보 등록
items = {
    'item1' : {'name': '상품1', 'price':8000},
    'item2' : {'name': '상품2', 'price':4000},
    'item3' : {'name': '상품1', 'price':5000}
}

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    if 'cart' not in session: # 세션에 cart가 없으면 
        session['cart'] = {} # 초기화
    
    # 카트에 물건 담기
    if item_name in session['cart']: # 세션에 있니? 있으면 담고 
        session['cart'][item_name] += 1
    else:
        session['cart'][item_name] = 1

    # 세션 데이터가 수정되었음을 flask에 알림
    session.modified = True # db 사용하면 쓸 필요x

    # 담은 이후 액션
    return redirect(url_for('index'))
    # index.html 페이지에서 상품명을 클릭해서 이 uri가 호출되게 구현하기


# 미션1. index.html 페이지에서 상품명을 클릭해서 이 URI가 호출되도록 구현
# 미션2. 장바구니 보기 버튼 추가
# 미션3. 장바구니 내용 세션을 통해 가져와서 cart.html에 출력
# 3-1 상품명, 갯수 출력
# 3-2 상품명, 개수, 개별단가 출력(내부 DB를 통해)
# 3-3 상품명, 개수, 토탈가격(개수 * 단가) 계산해서 출력
# 3-4 여러개의 상품명과 가격의 합산인 total 출력
@app.route('/view_cart')
def view_cart():
    # 세션에서 카트 정보를 가져와서 출력한다.
    cart_items = {}
    cart_items = session.get('cart')
    total = 0
    count = 0

    for item_name, quantity in session.get('cart', {}).items():
        item = items.get(item_name)
        if item:
            cart_items[item_name] = {'name': item['name'], 'quantity': quantity, 'price': item['price'], 'unit_price': (quantity*item['price'])}
            total += (quantity*item['price'])
            count += quantity
    return render_template('cart.html', cart_items=cart_items, total=total, count=count)


@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    # 상품 삭제
    session['cart'].pop(item_name)

    session.modified = True
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug = True, port=8080)