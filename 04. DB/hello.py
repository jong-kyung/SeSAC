import sqlite3

# DB 접속
conn = sqlite3.connect('hello.db')

# conn을 통해서 메시지를 주고 받음
# 로우레벨 접속을 한 소켓 인터페이스
# 커서(명령어를 주고 받는 위치)
c = conn.cursor()

user_input = 'user1'
pass_input = 'abcd1234'
# query = "SELECT username FROM user WHERE username=" + user_input

c.execute("SELECT * FROM user WHERE username=? AND password=?", (user_input, pass_input))
result = c.fetchall() # 가져오는 명령어
# result = c.fetchone() # 한개 가져옴
# result = c.fetchmany(3) # 파라미터를 넣으면 갯수만큼 가져옴
for r in result:
    print(r)

# 미션 로그인 코드 구현
if result:
    print('로그인에 성공했습니다')
else:
    print('로그인에 실패했습니다')

# DB 사용이 끝났을때, 변경사항들을 최종 기록
conn.commit()

# 접속을 종료
conn.close()