import sqlite3

# DB 접속
conn = sqlite3.connect('hello.db')

# conn을 통해서 메시지를 주고 받음
# 로우레벨 접속을 한 소켓 인터페이스
# 커서(명령어를 주고 받는 위치)
c = conn.cursor()