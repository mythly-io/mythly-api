from flask_restful import Resource

class Entity(Resource):
    def get(self, name):
        return {"message": name}, 200