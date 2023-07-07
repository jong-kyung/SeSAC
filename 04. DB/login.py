import sqlite3
import hashlib

conn = sqlite3.connect('hello.db')

c = conn.cursor()

username = input('사용자 이름을 입력하세요')
password = input('비밀번호를 입력하세요')

# 미션1. 사용자 콘솔로부터 username/password 를 받아서 처리해서 동작하는 함수를 구현하시오.

# 미션2. 암호화(단방향암호화) 처리해서 로그인 하는 코드 구현하기
# 2-1. 수동으로 username, password => username, hashed password 로 저장
# 2-2. 조회
def login(username, password):
    hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # c.execute("INSERT INTO user (username, password) VALUES (?,?)", (username, hashedPassword))
    # conn.commit()

    c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, hashedPassword))
    result= c.fetchall()
    if result:
        print('로그인 성공')
    else:
        print('로그인 실패')

# login(username, password)

# 강사님 방식인용 
def hash_password(password):
    hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashedPassword

def cleanup_table():
    c.execute('''DROP TABLE IF EXISTS user2''')
    conn.commit()
    c.execute('''CREATE TABLE user2(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
    conn.commit()

def insert_user():
    users=[
        ('user1','abcd1111'),
        ('user2','abcd2222'),
        ('user3','abcd3333'),
        ('user4','abcd4444'),
        ('user5','abcd5555'),
    ]
    
    for u in users:
        c.execute('INSERT INTO user2(username, password) VALUES (?,?)', (u[0], hash_password(u[1])))
    conn.commit()


def All_Data(tablename):
    c.execute(f"SELECT * FROM '{tablename}'")
    result = c.fetchall()
    print(result)

# 보안상 좋은 방법은 아님.
def login2(username, password):
    c.execute("SELECT * FROM user2 WHERE username=?", username)
    user = c.fetchone()
    
    if user is None:
        print('로그인 실패')
    else:
        stored_password = user[2]
        if hash_password(password) == stored_password:
            print('로그인 성공')

# 보안상 더 좋은 방법
def login3(username, password):
    input_password = hash_password(password)
    c.execute("SELECT * FROM user2 WHERE username=? AND password=?", (username, input_password))
    user = c.fetchone()
    
    if user is None:
        print('로그인 실패')
    else:
        print('로그인 성공')
