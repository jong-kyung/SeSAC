from selenium import webdriver
from selenium.webdriver.common.by import By # DOM 요소를 찾기 위한 import
from selenium.webdriver.chrome.options import Options

chrome_options = Options() # 브라우저 꺼짐 방지
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) #불필요한 에러 메세지 삭제
crawler = webdriver.Chrome(options = chrome_options) # Chrome Driver 실행 파라미터엔, 경로를 설정할 수 있음. 같은경로일 경우 공백

melonUrl = 'https://www.melon.com/chart/index.htm' # 내가 원하는 주소

crawler.get(melonUrl) # 실행
crawler.implicitly_wait(3) # 요소를 찾으려고 시도하기 전에 요소가 페이지에 있고 상호작용이 가능한 상태인지 확인

melon_chart_data = []

melon_chart_lists = crawler.find_elements(By.TAG_NAME, 'tr')

melon_song_names = crawler.find_elements(By.CSS_SELECTOR,'.wrap_song_info .rank01 a')
melon_song_artists = crawler.find_elements(By.CSS_SELECTOR, '.wrap_song_info .rank02')

for name,artist in zip(melon_song_names, melon_song_artists):
    print(f'제목:{name.text}, 가수:{artist.text}')

# crawler.quit() # 닫기