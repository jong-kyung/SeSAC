from flask import Flask, url_for, redirect, render_template, request
import requests
import json

app = Flask(__name__)

response = requests.get(
    'https://api.odcloud.kr/api/15111389/v1/uddi:41944402-8249-4e45-9e9d-a52d0a7db1cc?page=1&perPage=100&returnType=JSON&serviceKey=qzDwh%2FG2nfedt5exyx%2Bqs8dBntZgZXtElzrCykN%2F2FzMs9E6XU4W8To9IFal%2FPz1zCO98JDwi2Fs8AaQZiKOSw%3D%3D'
)
print(response.json())

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)