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
        # This function is returning all of the plants stock data from the plants_data table in the database.
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from plants_data") # This line performs query and returns json result
        return {'plants_data': [i for i in query.cursor.fetchall()]} # Fetches the data

class Plants_Name(Resource):
    def get(self, plant_name):
        # When a plant's name is entered into the plant_name input, this function returns all of that plant's data from the plants_data table in the database.
        conn = db_connect.connect()
        query = conn.execute(f"select * from plants_data where plant_name='{plant_name}'")
        return {'record': [i for i in query.cursor]} # Fetches the data


class Display_Quantity(Resource):
    def get(self, plant_name):
        # When a plant's name is entered into the plant_name input, this function returns the quantity of that plant from the plants_data table in the database.
        conn = db_connect.connect()
        query = conn.execute(f"select quantity from plants_data where plant_name='{plant_name}'")
        quantity = [i for i in query.cursor][0][0]
        return quantity

class Bought_Item(Resource):
    def get(self, plant_name):
        # When a plant's name is entered into the plant_name input, the function removes 1 item from that plant's quantity in the plants_data table in the database.
        conn = db_connect.connect()  # Connects to the database
        query = conn.execute(f"select quantity from plants_data where plant_name='{plant_name}'") # selects quantity with an SQL statement
        stock_quantity = [i for i in query.cursor][0][0] # puts the quantity of the plant into a variable so we can use it
        stock_quantity = stock_quantity - 1 # changes the variable and removes one item of stock from the quantity variable
        # executes the SQL statement which will update the plants_data table, sets the quantity of the stock to the new quantity.
        query = conn.execute(f"update plants_data set quantity='{stock_quantity}' where plant_name='{plant_name}'") 



api.add_resource(Plants, '/plants_data') # Route_1
api.add_resource(Plants_Name, '/plants_data/<plant_name>') 
api.add_resource(Display_Quantity, '/plants_data/<plant_name>/quantity')
api.add_resource(Bought_Item, '/plants_data/<plant_name>/purchase')


if __name__ == '__main__':
     app.run(port='5002')