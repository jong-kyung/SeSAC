import requests
from bs4 import BeautifulSoup

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

daum_movie_url = 'https://movie.daum.net'

rankings = soup.select('.list_movieranking > li')
for r in rankings:
    title = r.select_one('.link_txt')
    info = r.select('.info_txt')
    url = title['href']
    short = r.select_one('.link_story')
    print(f'제목:{title.text}, {info[0].text},{info[1].text}')
    print(f'링크{daum_movie_url + url}')
    print(f'쇼트:{short.text.strip()}')
