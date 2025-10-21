from flask import Flask, redirect, request, make_response, Response
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///notify.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api=Api(app)

class Welcome(Resource):
    def get(self):
        return "hi"
api.add_resource(Welcome, "/")

if __name__ =="__main__":
    app.run(debug=True)

