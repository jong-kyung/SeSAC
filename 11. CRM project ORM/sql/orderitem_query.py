from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

class OrderItem_query():   
    def __init__(self, TableName):
        self.TableName = TableName
        
    def total_data_query(self, page, count):
        datas = self.TableName.query\
         .offset((page-1) * count)\
        .limit(count)\
        .all()
        
        # 원하는 data 길이 불러오기
        data_length = self.TableName.query\
        .with_entities(func.count().label('data_count'))\
        .first()

        return {'datas':datas, 'data_length': data_length[0]}

    def find_data_query(self, column):
        result_datas = self.TableName.query.distinct(column).all()

        return result_datas

    def detail_info(self, FindData):
        result = self.TableName.query.filter(self.TableName.Id == FindData).first()

        return result