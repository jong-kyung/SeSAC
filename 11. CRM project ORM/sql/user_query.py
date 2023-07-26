from flask_sqlalchemy import SQLAlchemy

class User_query():   
    def __init__(self, TableName):
        self.TableName = TableName
    
    def total_data_query(self, page, count, *args):
        datas = self.TableName.query.offset((page-1) * count).limit(count).filter(self.TableName.Name.like(f'{args[0]}%'), self.TableName.Gender(f'%{args[1]}%')).all() # 원하는 데이터 가져오기
        
        data_length = db.session.query(func.count('*').label('data_count')).filter(self.TableName.Name.like(f'{args[0]}%'), self.TableName.Gender(f'%{args[1]}%')).first()

        return {'datas': datas, 'data_length': data_length}

    def find_data_query(self, column):
        result_datas = self.TableName.query.distinct(column).all()

        return result_datas

    def detail_info(self, FindData):
        result = self.TableName.query.filter(self.TableName.Id == FindData).first()

        return result
    
    # def store_rate(self, UserID):
    #     result = db.session.query(users, stores, orders, orderitems)\
    #             .join(stores, orders.StoreId == stores.Id)\
    #             .join(orderitems, orders.Id == orderitems.Id)\
    #             .join(users, orders.UserId == users.Id)\
    #             .filter(users.Id = UserID)\
    #             .group_by(stores.Name)\
    #             .limit(5).all()

    #     return result