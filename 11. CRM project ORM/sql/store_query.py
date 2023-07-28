from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
from __init__ import db
class Store_query():   
    def __init__(self, TableName):
        self.TableName = TableName
    
    def total_data_query(self, page, count, *args):
        datas = self.TableName.query\
        .filter(self.TableName.Name.like(f'{args[0]}%'))\
        .filter(self.TableName.Type.like(f'%{args[1]}%'))\
        .offset((page-1) * count)\
        .limit(count)\
        .all()
        
        data_length = self.TableName.query\
        .with_entities(func.count().label('data_count'))\
        .filter(self.TableName.Name.like(f'{args[0]}%'))\
        .filter(self.TableName.Type.like(f'%{args[1]}%'))\
        .first()

        return {'datas': datas, 'data_length': data_length[0]}

    def find_data_query(self, column):
        result_datas = self.TableName.query.distinct(column).all()

        return result_datas

    def detail_info(self, FindData):
        result = self.TableName.query.filter(self.TableName.Id == FindData).first()

        return result

    def monthly_sale(self, store_ID):
        query = text(f"""
            SELECT substr(orders.OrderAt, 1, 7) AS Month, SUM(items.price) AS Revenue, count(items.Id) AS count
            FROM stores
            INNER JOIN orders ON stores.Id = orders.StoreId
            INNER JOIN orderitems ON orders.Id = orderitems.OrderId
            INNER JOIN items ON orderitems.ItemId = items.Id
            WHERE stores.Id = :store_id
            GROUP BY stores.Name, Month
            ORDER BY Month
        """)
        result = db.session.execute(query, {'store_id': store_ID}).fetchall()

        return result
    
    def visit_users(self, store_ID):
        query = text(f'''SELECT users.Id, users.name, count(orders.StoreID) AS count FROM users 
                            INNER JOIN orders ON users.Id = orders.UserId
                            WHERE orders.StoreId = '{store_ID}'
                            GROUP BY users.name
                            ORDER BY count DESC
                            ''')
    
        result = db.session.execute(query, {'store_id': store_ID}).fetchall()
        return result


    def city_frequency(self):
        query = text(f'''SELECT 
            SUBSTR(address, INSTR(address, ' ') + 1, INSTR(SUBSTR(address, INSTR(address, ' ') + 1), ' ') - 1) AS city, count(address)
            FROM stores GROUP BY city''')
        
        result = db.session.execute(query).fetchall()

        return result