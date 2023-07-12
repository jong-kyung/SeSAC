from flask import Flask, render_template
import sqlite3

app=Flask(__name__) 
print('hello')

@app.route('/')
def index():
    # TODO : 월간 매출액 합산을 구하시오
    conn = sqlite3.connect('./DB/crm.db')

    cursor = conn.cursor()

    cursor.execute("SELECT substr(orders.OrderAt,1, 4) AS 'Year', substr(orders.OrderAt, 6, 2) AS 'Month', stores.name, SUM(items.UnitPrice) AS 'Total' FROM orders INNER JOIN stores ON orders.storeId = stores.Id INNER JOIN orderitems ON  orders.Id = orderitems.Orderid INNER JOIN items ON orderitems.ItemId = items.Id WHERE stores.name = '커피빈 홍대6호점' GROUP BY Year, Month")
    rows = cursor.fetchall()
    
    labels = []
    revenues = []
    for row in rows:
        labels.append(row[1])
        revenues.append(row[3])
    conn.close()
    return render_template('index.html', rows=rows, labels = labels, revenues = revenues)

if __name__ == '__main__':
    app.run(debug=True, port=8080)