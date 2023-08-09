import os
import sys
import json
import urllib.request # 파이썬 내장 라이브러리임.

client_id = "sInGF4qWfuda2Nztl_2K" # 개발자센터에서 발급받은 Client ID 값
client_secret = open('secret.txt', 'r').read() # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText # 소스는 한국어인데 영어로 변경하겠다는걸 url에 남겨둠
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    print('-'*50)
    data = json.loads(response_body) # json으로 변경
    print(data['message']['result']['translatedText']) # 번역된 결과만 출력
else:
    print("Error Code:" + rescode)


# curl "https://openapi.naver.com/v1/papago/n2mt" \
# -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
# -H "X-Naver-Client-Id: sInGF4qWfuda2Nztl_2K" \
# -H "X-Naver-Client-Secret: 2qo9JurUcz" \
# -d "source=ko&target=en&text=만나서 반갑습니다." -v