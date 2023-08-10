from flask import Flask, request
from flask_restx import Api, Resource # API문서화를 자동으로 해주는 도구

app = Flask(__name__)
api = Api(app) # app을 Api객체에 등록

todos = {}

@api.route('/<string:todo_id>')
class Todo(Resource): # Resource상속을 통해 Api함수라는것을 정의해줌
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}

if __name__ == '__main__':
    app.run(debug = True, port = 8080)