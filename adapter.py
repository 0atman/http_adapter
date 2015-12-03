from flask import Flask
from flask_restful import Api

from routes import *


app = Flask(__name__)
api = Api(app)

map(lambda routes: api.add_resource(routes[0], routes[1]), routes)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
