from flask import Flask
from flask_restx import Api, Resource # API문서화를 자동으로 해주는 도구

app = Flask(__name__)
api = Api(app) # app을 Api객체에 등록

@api.route('/hello')
class HelloWorld(Resource): # Resource상속을 통해 Api함수라는것을 정의해줌
    def get(self):
        return "{'hello':'world'}"

if __name__ == '__main__':
    app.run(debug = True, port = 8080)