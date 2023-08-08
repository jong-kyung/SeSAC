import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import date

# 데이터베이스 설정
conn = sqlite3.connect('movie_data.db')
cur = conn.cursor()

# 테이블 생성
cur.execute('''
    CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            rating TEXT,
            poster_url TEXT,
            short_description TEXT
    )
''')       

# ! RANKING, DATE용 테이블
cur.execute('''
    CREATE TABLE IF NOT EXISTS weekly_rankings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ranking TEXT, 
                updated_at DATETIME,
                movie_id INTEGER,
                FOREIGN KEY(movie_id) REFERENCES moives(id)
    )
''')
conn.commit()

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

daum_movie_url = 'https://movie.daum.net'

rankings = soup.select('.list_movieranking > li')
for r in rankings:
    title = r.select_one('.link_txt')
    info = r.select('.info_txt')
    url = title['href']
    short = r.select_one('.link_story')
    today = date.today()
    
    cur.execute('INSERT INTO movies (title, rating, poster_url, short_description) VALUES (?, ?, ?, ?)',(title.text, info[0].text.replace("평점",""), daum_movie_url + url, short.text.strip())) # movie 테이블에 DB 삽입
    movie_id = cur.lastrowid # insert한 id값 가져오기
    cur.execute('INSERT INTO weekly_rankings (ranking, updated_at, movie_id) VALUES (?, ?, ?)',(info[1].text.replace("예매율",""), today, movie_id))
    conn.commit()

    # 만약 8월 9일인데 같은영화가 순위권에 존재하면 ??..
    # 평점이 달라지는정도일텐데.. ?..  update를 통해 평점을 변경해주고..
    # 그렇게 되면 순위도 바뀔텐데 .. ? ranking(예매율)값도 바꿔줘야겠네


