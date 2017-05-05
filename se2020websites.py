from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)


# circlejerk function
class randomSEwebsite(Resource):
    def get(self):
        websites = {
            "Arash": "http://arashrai.com",
            "Stephen": "https://melinysh.me",
            "James": "http://jameshageman.com",
            "Matt": "http://mattdsouza.com",
            "Holly": "http://hollyoegema.com"
        }
        return random.choice(list(websites.values()))


api.add_resource(randomSEwebsite, '/randomSEwebsite')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
