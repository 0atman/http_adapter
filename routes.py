from flask_restful import Resource


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: 1}

    def put(self, todo_id):
        return {todo_id: 1}

routes = [
    (TodoSimple, '/test2/<string:todo_id>')
]
