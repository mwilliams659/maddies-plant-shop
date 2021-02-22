from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from flask_cors import CORS
import datetime

def db_connect():
    return create_engine('sqlite:///../database/plants_database.db')

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5500"}})


@app.route("/plants_data")
def get_all_plants_data():
    # This function is returning all of the plants stock data from the plants_data table in the database.
    conn = db_connect().connect() # connect to database
    query = conn.execute("select * from plants_data") # This line performs query and returns json result
    all_plants_data = [i for i in query.cursor.fetchall()]
    return {'plants_data': all_plants_data} # Fetches the data
    
@app.route("/plants_data/<plant_name>")
def get_single_plant_data(plant_name):
    # When a plant's name is entered into the plant_name input, this function returns all of that plant's data from the plants_data table in the database.
    conn = db_connect().connect() # connect to database
    query = conn.execute(f"select * from plants_data where plant_name='{plant_name}'")
    return {'record': [i for i in query.cursor]} # Fetches the data

@app.route("/plants_data/<plant_name>/price")
def get_plant_price(plant_name):
    # When a plant's name is entered into the plant_name input, this function returns the price of that plant from the plants_data table in the database.
    conn = db_connect().connect() # connect to database
    query = conn.execute(f"select price from plants_data where plant_name='{plant_name}'")
    price = [i for i in query.cursor][0][0]
    return str(price)

@app.route("/plants_data/<plant_name>/quantity")
def get_plant_quantity(plant_name):
    # When a plant's name is entered into the plant_name input, this function returns the quantity of that plant from the plants_data table in the database.
    conn = db_connect().connect() # connect to database
    query = conn.execute(f"select quantity from plants_data where plant_name='{plant_name}'")
    quantity = ([i for i in query.cursor][0][0])
    return str(quantity)

@app.route('/plants_data/<plant_name>/purchase')
def single_plant_bought(plant_name):
    # When a plant's name is entered into the plant_name input, the function removes 1 item from that plant's quantity in the plants_data table in the database.
    old_quantity = int(get_plant_quantity(plant_name))
    new_quantity = old_quantity - 1 # changes the variable and removes one item of stock from the quantity variable
    update_quantity(plant_name, new_quantity)
    return f"One {plant_name} bought" 


def update_quantity(plant_name, quantity):
    conn = db_connect().connect()
    # executes the SQL statement which will update the plants_data table, sets the quantity of the stock to the new quantity.
    query = conn.execute(f"update plants_data set quantity='{quantity}' where plant_name='{plant_name}'")
    return f"{plant_name} quantity updated to {quantity}"

@app.route('/plants_data/<plant_name>/<quantity>/<cart_id>')
def add_to_basket(cart_id, plant_name, quantity):
    conn = db_connect().connect()
    price = get_plant_price(plant_name)
    time_stamp = datetime.datetime.now()
    query = conn.execute(f"INSERT INTO basket_table (id, plant_name, cart_id, price, quantity, created_at, updated_at) VALUES (1, '{plant_name}', '{cart_id}', '{price}', '{quantity}', '{time_stamp}', 'time');")
    return f"{plant_name} added to basket"

#function which will get one record from the basket_table table
def get_record_from_basket_table(cart_id):
    conn = db_connect().connect() # connect to database
    query = conn.execute(f"select * from basket_table where cart_id='{cart_id}'")
    return {'record': [i for i in query.cursor]} # Fetches the data

#function which will remove one record from the plants_data table
def remove_record_from_basket_table(cart_id):
    conn = db_connect().connect()
    query = conn.execute(f"delete from basket_table where cart_id='{cart_id}'")
    

if __name__ == '__main__':
     app.run(port='5002')