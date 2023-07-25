from flask import Flask, render_template, redirect, url_for, session, request
from flask import flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'random text' # 랜덤값으로 넣어주는게 보안에 좋음
app.permanent_session_lifetime = timedelta(minutes = 1) # session 지속시간 설정

@app.route('/' , methods=['GET', 'POST'])
def home():
    name = None
    age = None
    flash('메시지 테스트')
    if request.method == 'GET':
        name = request.args.get('name', default='')
        age = request.args.get('age', default='')
    elif request.method == 'POST':
        name = request.form['name']
        session['userid'] = name # session에 값 넣기
        session.permanent = True
        flash('Login Success')
        flash('메시지 플래싱 예제입니다')
    else:
        return 'UNKNOWN METHOD'
    
    return render_template('index.html', name=name, age=age)

@app.route('/user')
def user():
    if 'userid' in session:
        user = session['userid']
        return f'<h1>hellot, {user}</h1>'
    else :
        return redirect(url_for('home'))

@app.route('/redirect')
def redirect_root():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)