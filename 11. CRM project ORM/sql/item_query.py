from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text

class Item_query():   
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
