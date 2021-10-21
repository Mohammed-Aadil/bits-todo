from flask import Flask
from flask import jsonify
from flask.views import MethodView
from service import Todo

app = Flask(__name__)

class TodoAPI(MethodView):
    def get(self):
        return jsonify(Todo().get()), 200
    
    def post(self):
        return jsonify(Todo().create()), 200
    
    def put(self, todo_id):
        return jsonify(Todo().update(todo_id=todo_id)), 200
    
    def delete(self, todo_id):
        return jsonify(Todo().delete(todo_id=todo_id)), 200

view = TodoAPI.as_view('todo_api')
app.add_url_rule('/todo', view_func=view, methods=['POST', 'GET'])
app.add_url_rule('/todo/<string:todo_id>', view_func=view, methods=['PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)