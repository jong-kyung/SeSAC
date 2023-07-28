from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key' # 암호화 키
# ! app['SECRET_KEY'] 오타가 나면 오류를 확인할 수 없기 때문에 위 방식이 코딩적으로는 더 좋음

# DB 초기화
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session.db'
db = SQLAlchemy(app)

# flask_session 설정
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

# 세션 저장을 위한 DB 저장소 설계
class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key = True)
    data = db.Column(db.Text)

# 내가 원하는 데이터 내용을 DB의 data라는 변수에 저자하기 위한 함수
def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id =sid)

    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()

# 세션 데이터 가져오는 함수
def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data:
        return json.loads(session_data.data)

@app.route('/')
def index():
    session['username'] = 'user'
    session['data'] = '1234'

    # 숫자 데이터 저장
    session['count'] = 42

    # 리스트 데이터 저장
    session['my_list'] = [1,2,3,4,5]

    # 세션 데이터 저장
    session_store(session.sid, dict(session))

    return 'Hello'

@app.route('/get_session')
def get_session_data_route():
    username = session.get('username')
    data = session.get('data')
    
    # 저장된 데이터 가져오기
    stored_session_data = get_session_data(session.sid)
    print(stored_session_data)

    # 세션 데이터를 화면에 출력 가능한 형태로 변경
    stored_session_str = json.dumps(stored_session_data, indent=4)

    return f'Username : {username}, {data}, my-data:{stored_session_str}'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port = 8080, debug = True)