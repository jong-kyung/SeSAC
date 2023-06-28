# 웹크롤링
import requests

# 추가 패키지 설치
# 파이썬 내에서 추가 패키지 하는 방법
# pip install / conda install 설치시 가상환경에 설치됨

# 네이버 페이지의 내용을 받아와서 화면에 텍스트로 출력하시오
response = requests.get('https://movie.daum.net/main')
response.text

# 네이버 페이지 내에서 가져온 컨텐츠 내에서 h2 태그로 작성된 컨텐츠 찾기
search_str = "h2"
contents = response.text

for line in contents.splitlines(): # splitlines() : 줄단위로 자르기
    if search_str in line:
        print(line.strip()) # strip() : 문자열 공백 제거
