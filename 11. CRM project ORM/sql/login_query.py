from flask_sqlalchemy import SQLAlchemy

class Login_query():
    def __init__(self, TableName):
        self.TableName = TableName

    def check_overlap(self, param): # 중복계정 확인
        user_id = self.TableName.query.with_entities(self.TableName.Username).filter(self.TableName.Username == param).first() # SELECT

        return user_id
    
    def insert_user_id(self, user_id): # auth에 사용자 정보 등록
        new_user = self.TableName(Id = user_id[0], Username = user_id[1], Password = user_id[2])
        db.session.add(new_user)
        db.session.commit()

    def user_auth(self, id, pw): # 로그인시 사용자 확인
        find_uesr_id = self.TableName.query.with_entities(self.TableName.Username, self.TableName.Password).filter(self.TableName.Username == id, self.TableName.Password == pw).first()
        
        return find_uesr_id

    def insert_user_info(self, user_info): # crm에 사용자 정보 삽입
        new_user = self.TableName(Id = user_info[0], Name = user_info[1], Gender = user_info[2], Birthdate = user_info[3], Address = user_info[4])
        db.session.add(new_user)
        db.session.commit()

    def user_info(self, user_name): # 사용자의 신원에 따라 보여주는 페이지 조절
        user_cert = self.TableName.query.with_entities(self.TableName.Username).filter(self.TableName.Username == user_name ).first()
        
        return user_cert

