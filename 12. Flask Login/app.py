from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

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

# DB 마이그레이션 모듈 로딩
migrate = Migrate(app, db)

# 로그인 매니저 생성
login_manager = LoginManager(app)
login_manager.login_view = 'login' # 로그인 페이지 URI 설정

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    # password_hash = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120))

    def set_password(self, password): # 해시값으로 전환
        self.password = password
        # self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return self.password == password
        # return check_password_hash(self.password_hash, password)

@login_manager.user_loader # 로그인을 하기 위한 함수
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form['username']
        pw = request.form['password']
        find_user = User.query.filter(User.username == id).first()

        if find_user and find_user.check_password(pw):
            login_user(find_user) # 로그인 정보 저장
            return redirect(url_for('view_users'))
        else:
            flash('계정이 없거나 비밀번호가 틀립니다.', 'danger')
    else:
        return redirect(url_for('main'))
    
@app.route('/logout')
@login_required
def logout():
    logout_user() # 로그아웃
    flash('로그아웃 되었습니다.', 'danger')
    return redirect('/')

@app.route('/profile_edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    if request.method == 'POST':
        new_pw = request.form['pw']
        new_email = request.form['email']
        current_user.password = new_pw
        current_user.email = new_email
        db.session.commit()
        flash('사용자 정보가 수정되었습니다', 'success')
        return redirect(url_for('view_users'))
    else: 
        return render_template('profile_edit.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['username']
        pw = request.form['password']
        email = request.form['email']
        
        existing_user = User.query.filter_by(username = id).first()
        if existing_user:
            flash('중복된 사용자입니다')
            return redirect(url_for('register'))

        new_user = User(username = id, email = email)
        new_user.set_password(pw)
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입이 되었습니다! 로그인을 해주세요!', 'info')
        return redirect(url_for('main'))
    else:
        return render_template('register.html')

@app.route('/users')
@login_required
def view_users():
    users = User.query.all()
    return render_template('users.html', users = users) 

@app.route('/withdraw')
@login_required
def withdraw():
    db.session.delete(current_user)
    db.session.commit()
    flash('헤어지게 되어 아쉬워요 다음에 또 뵐 수 있기를 바랄게요 :)', 'warning')
    return redirect(url_for('main'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port = 8080, debug = True)