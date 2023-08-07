import requests
from bs4 import BeautifulSoup


def get_sportsnews():
    data = requests.get('https://sports.news.naver.com/index')
    soup = BeautifulSoup(data.text, 'html.parser')

    naver_news_url = 'https://sports.news.naver.com/index'

    # print(soup)
    news = soup.select('.today_list > li')
    # print(len(news))

    for n in news:
        # 미션 타이틀제목을 가져온다
        title = n.select_one('.title')
        print(title.text.strip())

        a_tag = n.select_one('a')
        print(naver_news_url + a_tag['href'])
        print(a_tag['title'])

def print_news_content(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    news_content = soup.select_one('.news_end')
    if news_content: 
        start_span = news_content.find('span')
        end_p = news_content.find('p', class_= 'source')
        if start_span and end_p:
            content = start_span.next_element
            while content and content != end_p:
                if isinstance(content, str) and content.strip():
                    print(content.strip())
                content = content.next_element
    
    print('-'*20)

def get_naver_land():
    data = requests.get('https://land.naver.com/news/')
    soup = BeautifulSoup(data.text, 'html.parser')

    naver_land_url = 'https://land.naver.com/' # 부동산 링크받기

    # 미션1 분야별 헤드라인 정보를 가져온다
    headlines = soup.select('.list_type')[0]
    lis = headlines.select('li')
    for li in lis:
        title = li.select('a') # a태그들 선택
        news_detail_url = naver_land_url + title[1]['href'] # 디테일들의 경로 설정
        detail_data = requests.get(news_detail_url) # 경로 적용
        detail_soup = BeautifulSoup(detail_data.text, 'html.parser')

        article = detail_soup.select_one('#articleBody')
        print(f'제목:{title[1].text.strip()}내용:{article.text}')
        
    # 미션2. 동향보고서 내용을 가져온다.
    reports = soup.select('.list_type')[1]
    reports_lis = reports.select('li')
    for li in reports_lis:
        report = li.select_one('a')
        print(report.text)


if __name__ == '__main__':
    # get_sportsnews()
    get_naver_land()