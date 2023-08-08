from flask import Flask, render_template, request
import sqlite3

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
        result_datas.append({'title': data[1], 'rating':data[2], 'link':data[3], 'shorts':data[4], 'reserv': data[5]})
    return render_template('detail.html', datas = result_datas)


if __name__ == "__main__":
    app.run(port=8080, debug=True)