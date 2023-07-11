from webdriver_manager.chrome import ChromeDriverManager # 브라우저 최신버전 업데이트를 위한 모듈 
from selenium import webdriver
from selenium.webdriver.common.by import By # DOM 요소를 찾기 위한 import
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def crawl_browser(URL, FindTitles, FindArtists, FindAlbums):
    chrome_options = Options() # 브라우저 꺼짐 방지
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) #불필요한 에러 메세지 삭제
    service = Service(executable_path = ChromeDriverManager().install())
    crawler = webdriver.Chrome(service = service ,options = chrome_options) # Chrome Driver 실행 파라미터엔, 경로를 설정할 수 있음. 같은경로일 경우 공백
    datas = []
    crawler.get(URL) # 실행

    crawler.implicitly_wait(3) # 요소를 찾으려고 시도하기 전에 요소가 페이지에 있고 상호작용이 가능한 상태인지 확인
    
    titles = crawler.find_elements(By.CSS_SELECTOR, FindTitles)
    artists = crawler.find_elements(By.CSS_SELECTOR, FindArtists)
    albums = crawler.find_elements(By.CSS_SELECTOR, FindAlbums)

    for title, artist, album in zip(titles, artists, albums):
        datas.append({
            'Title': title.text,
            'Artist': artist.text,
            'AlbumTitle': album.text
        })
    crawler.quit() # 닫기
    return datas

