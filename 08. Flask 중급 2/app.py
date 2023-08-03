from flask import Flask, render_template, redirect, url_for, flash, request, session

app = Flask(__name__)

app.secret_key = 'this_is_my_secret_key'

# 가상의 사용자 테이블
users = {
    'user1' : {'password': 'password1234'},
    'user2' : {'password': 'abc123'}
}

@app.route('/')
def home():
    if 'username' in session:
        flash('로그인에 성공하셨습니다.')
        username = session['username']
        return render_template('index.html', username=username)
    
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # DB를 통해서 로그인 확인 - 지금은 가상 테이블
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('로그인에 실패하였습니다.')
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=8080, debug=True)

# 미션1. 렌더템플릿을 통해서 첫 화면에 login/logout 추가
# 미션2. 로그인 성공실패 여부를 flash 메시지 통해서 처리
# 미션3. 디자인 적용해서 flash 메시지 색상 다르게 해보기 (성공시 초록, 실패시 빨강)