from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

"""
LoginManager: 로그인 관리를 담당하는 클래스로, Flask 애플리케이션에서 로그인 기능을 초기화하고 관리하는 역할을 합니다.
UserMixin: UserMixin 클래스는 Flask-Login이 기본적으로 사용하는 사용자 모델 클래스를 정의하기 위해 사용됩니다. 이 클래스를 사용하여 사용자 모델 클래스에 필요한 메서드들을 간단하게 추가할 수 있습니다.
login_user: 로그인 처리를 위해 사용되는 함수로, 인증이 성공적으로 완료된 사용자를 로그인 상태로 만듭니다. 이 함수를 호출하면 세션에 사용자 정보가 저장되어 사용자를 인증된 상태로 유지할 수 있습니다.
login_required: 데코레이터로, 특정 뷰 함수를 보호하는 데 사용됩니다. 이 데코레이터가 적용된 뷰 함수는 로그인된 사용자만 접근할 수 있으며, 로그인되지 않은 사용자는 로그인 페이지로 리디렉션됩니다.
logout_user: 로그아웃 처리를 위해 사용되는 함수로, 현재 로그인된 사용자를 로그아웃 상태로 만듭니다. 세션에서 사용자 정보를 삭제하여 인증을 끝내는 역할을 합니다.
current_user: 현재 로그인된 사용자를 나타내는 객체입니다. 로그인되지 않은 경우 AnonymousUserMixin 객체가 반환됩니다. 이를 통해 로그인된 사용자의 정보를 뷰 함수에서 간단하게 접근할 수 있습니다.
"""

app = Flask(__name__)

# 환경설정
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATONS'] = False

# DB 생성
db = SQLAlchemy(app)

# 로그인 매니저 생성
login_manager = LoginManager(app)
login_manager.login_view = 'login' # 로그인 페이지 URI 설정

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120))

@login_manager.user_loader # 로그인을 하기 위한 함수
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    # 로그인 기능 구현
    # 1. form으로 부터 id/pw 를 받아온다
    # 2. DB로 부터 쿼리해서 id/pw가 맞는지 확인한다
    # 3. 성공하면 로그인정보를 저장하고 로그인 한 페이지로 이동
    #    실패하면 오류를 알려준다
    if request.method == 'POST':
        id = request.form['username']
        pw = request.form['password']
        find_user = User.query.filter(User.username == id, User.password == pw).first()

        if find_user:
            login_user(find_user) # 로그인 정보 저장
            return redirect(url_for('view_users'))
        else:
            return '로그인 실패!'
    else:
        return redirect(url_for('main'))
    
@app.route('/logout')
@login_required
def logout():
    logout_user() # 로그아웃
    return redirect(url_for('main'))

@app.route('/profile_edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    # 미션 : 프로필 수정기능 구현
    # 1. 폼을 통해 변경하려는 내역을 가져온다(password)
    # 2. 저장할 장소를 가져온다. (current_user 이용)
    # 3. 받아온 정보를 DB에 저장한다
    if request.method == 'POST':
        new_pw = request.form['pw']
        new_email = request.form['email']
        current_user.password = new_pw
        current_user.email = new_email
        db.session.commit()

        return redirect(url_for('main'))
    else: 
        return render_template('profile_edit.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # 회원가입 form을 만든다
    # 회원기입 정보를 가져온다
    # DB에 저장한다
    if request.method == 'POST':
        id = request.form['username']
        pw = request.form['password']
        email = request.form['email']

        new_user = User(username = id, password = pw, email = email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main'))
    else:
        return render_template('register.html')

@app.route('/users')
@login_required
def view_users():
    # 모든 사용자 보여주기
    # 1. 사용자 정보를 모두 조회한다
    # 2. HTML 조회한 정보를 전달해 출력한다
    users = User.query.all()
    return render_template('users.html', users = users) 

@app.route('/withdraw')
@login_required
def withdraw():
    db.session.delete(current_user)
    db.session.commit()
    return redirect(url_for('main'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port = 8080, debug = True)