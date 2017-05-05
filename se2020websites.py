from flask import Flask, redirect
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
            "Holly": "http://hollyoegema.com",
            "George": "http://georgeutsin.com/",
            "Spencer": "http://spencerdobrik.com/",
            "Liam": "http://liamca.xyz/",
            "Ryan": "http://www.ryan-martin.ca/",
            "Denton": "http://dentonliu.com/",
            "Stanley": "http://stanhuan.com/",
            "Prilik": "http://prilik.com/"
        }
        lucker_dog = random.choice(list(websites.values()))
        return redirect(lucker_dog, code=302)


api.add_resource(randomSEwebsite, '/randomSEwebsite')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
