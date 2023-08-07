import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.pythonscraping.com/pages/page3.html')

# print(data)
# print(data.text)

soup = BeautifulSoup(data.text, 'html.parser') # html

# print(soup)

gifts = soup.select('#giftList > tr') # 선택자 이용해서 내용 불러오기
# print(len(gifts))

my_gifts = gifts[1:] # list slicing
# print(len(my_gifts))

for g in my_gifts:
    # print(g)
    tds = g.select('td')
    print(f'title:{tds[0].text.strip()}, price:{tds[2].text.strip()}')
    print(f'picture:{tds[3].img["src"]}')