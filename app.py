from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from config import env_vars

from resources.entity import Entity

app = Flask(__name__)
api = Api(app)

api.add_resource(Entity, "/entity/<string:name>")

if __name__ == "__main__":
    app.run(port=env_vars["port"], debug=True)