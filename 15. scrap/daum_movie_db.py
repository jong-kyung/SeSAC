import requests
from bs4 import BeautifulSoup
import sqlite3

# 데이터베이스 설정
conn = sqlite3.connect('movie_data.db')
cur = conn.cursor()

# 테이블 생성
cur.execute('''
    CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            rating TEXT,
            reservation_rate TEXT,
            poster_url TEXT,
            short_description TEXT,
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
    # print(f'제목:{title.text}, {info[0].text.replace("평점","")},{info[1].text.replace("예매율","")}')
    # print(f'링크{daum_movie_url + url}')
    # print(f'쇼트:{short.text.strip()}')
    
    cur.execute('INSERT INTO movies (title, rating, reservation_rate, poster_url, short_description) VALUES (?, ?, ?, ?, ?)',(title.text, info[0].text.replace("평점",""), info[1].text.replace("예매율",""), daum_movie_url + url, short.text.strip()))
    conn.commit()