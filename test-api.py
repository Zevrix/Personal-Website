from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

# Create a engine for connecting to SQLite3.
# Assuming salaries.db is in your app root folder


app = Flask(__name__)
api = Api(app)


class Departments_Meta(Resource):
    def get(self):
        return {'departments': 3}


class Departmental_Salary(Resource):
    def get(self, department_name):
        result = {'data': 'tessst'}
        return result
        # We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
