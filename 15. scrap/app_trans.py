from flask import Flask, render_template, request
import sqlite3
import json
import urllib.request # 파이썬 내장 라이브러리임.

# DB 
conn = sqlite3.connect('movie_data.db', check_same_thread=False)
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    dates = []
    cursor.execute("SELECT DISTINCT updated_at FROM weekly_rankings")
    datas = cursor.fetchall()
    for data in datas:
        dates.append({'date':data[0]})
    print(dates)
    return render_template('index.html', dates = dates)

@app.route('/<param>')
def movie_info(param):
    result_datas = []
    cursor.execute("SELECT movies.*, weekly_rankings.ranking FROM movies JOIN weekly_rankings ON movies.id = weekly_rankings.movie_id WHERE weekly_rankings.updated_at = ?", (param, ))
    datas = cursor.fetchall()
    for data in datas:
        eng_shotrs = trans_kor_eng(data[4])
        result_datas.append({'title': data[1], 'rating':data[2], 'link':data[3], 'shorts':eng_shotrs, 'reserv': data[5]})
    return render_template('detail.html', datas = result_datas)

def trans_kor_eng(param):
    client_id = "sInGF4qWfuda2Nztl_2K" 
    client_secret = open('secret.txt', 'r').read()
    encText = urllib.parse.quote(param)
    data = "source=ko&target=en&text=" + encText 
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        data = json.loads(response_body) # json으로 변경
        return data['message']['result']['translatedText']
    
    else:
        print("Error Code:" + rescode)


if __name__ == "__main__":
    app.run(port=8080, debug=True)