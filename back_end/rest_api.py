from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
    
db_connect = create_engine('sqlite:///plants_database.db')
app = Flask(__name__)
api = Api(app)

class Plants(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from plants_data") # This line performs query and returns json result
        return {'plants_data': [i for i in query.cursor.fetchall()]} # Fetches the data

class Plants_Name(Resource):
    def get(self, plant_name):
        conn = db_connect.connect()
        query = conn.execute(f"select * from plants_data where plant_name='{plant_name}'")
        return {'record': [i for i in query.cursor]} # Fetches the data


api.add_resource(Plants, '/plants_data') # Route_1
api.add_resource(Plants_Name, '/plants_data/<plant_name>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')