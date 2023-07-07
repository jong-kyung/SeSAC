import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT)''')

# 몇 명의 사용자 추가
users = [
    ('John Doe', 25, 'Male'),
    ('Jane Smith', 30, 'Female'),
    ('Michael Johnson', 35, 'Male'),
    ('Emily Davis', 28, 'Female'),
    ('David Lee', 32, 'Male'),
    ('Emma Wilson', 27, 'Female'),
    ('Daniel Brown', 31, 'Male'),
    ('Olivia Taylor', 29, 'Female'),
    ('Sophia Anderson', 33, 'Female'),
    ('Matthew Martin', 26, 'Male')
]

# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# 변경사항 저장
conn.commit()

#-----------------------
# 여기 이후에 원하는 쿼리문 추가
#-----------------------

# 미션1. 성별이 여자인 사람만 출력
cursor.execute("SELECT * FROM users WHERE gender='Female'")
result = cursor.fetchall()
print('--------여자--------')
for user in result:
    print(user)

# 미션2. 나이가 30살 이상인 사람만 출력
cursor.execute("SELECT * FROM users WHERE age>=30")
result = cursor.fetchall()
print('--------30살이상--------')
for user in result:
    print(user)

# 미션3. 나이가 25세 이상 30세 이하인 사용자 출력
cursor.execute("SELECT * FROM users WHERE age BETWEEN 25 AND 30")
result = cursor.fetchall()
print('--------25살 이상 30살 이하--------')
for user in result:
    print(user)

# 미션4. 성별로 그룹핑(남/여 각각) 몇명인지 출력
cursor.execute("SELECT gender, COUNT(*) FROM users GROUP BY gender")
result = cursor.fetchall()
print('--------남/여통계--------')
for gender, count in result:
    print(f"성별 :{gender}:{count}")

# 미션5. John Doe의 나이를 25살 -> 26살로 업데이트하기
cursor.execute("UPDATE users SET age=26 WHERE name='John Doe'")
conn.commit()

cursor.execute("SELECT * FROM users WHERE name='John Doe'")
result = cursor.fetchall()
print(result)

# 미션6. Emily Davis 사용자 데이터 삭제하기.
cursor.execute("DELETE FROM users WHERE name='Emily Davis'")
cursor.execute("SELECT * FROM users WHERE name='Emily Davis'")
result = cursor.fetchall()
print(result)

conn.close()