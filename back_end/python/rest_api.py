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
CORS(app)


# table browser functions
#single plant data
@app.route("/browser_plants_data/<plant_name>")
def get_single_plant_data_browser(plant_name):
    data = get_single_plant_data(plant_name)
    # data = data["record"][0]
    plant_type = data["record"][0][1]
    quantity = data["record"][0][2]
    price = data["record"][0][3]
    return f"""

    <table style="background-color:#67c16a;font-family:monospace;font-size:32px;width:100%;border:4px solid black;
  border-collapse:collapse;padding:15px;
  text-align:center;">
        <caption>Single Plant Data Table</caption
        <tr style="border: 2px solid black;">
            <th>Plant Name</th>
            <th>Plant Type</th>
            <th>Quantity</th>
            <th>Price</th>
        </tr>
        <tr style="background-color: #ccffcc;">
            <td>{plant_name}</td>
            <td>{plant_type}</td>
            <td>{quantity}</td>
            <td>{price}</td>
        </tr>
    </table>
    """

#all data
@app.route("/browser_plants_data")
def get_all_plant_data_browser():
    data = get_all_plants_data()
    data = data["plants_data"]
    print(data)
    info = f"""

    <table style="background-color:#67c16a;font-family:monospace;font-size:32px;width:100%;border:4px solid black;
  border-collapse:collapse;padding:15px;
  text-align:center;">
        <caption>Plants Data Table</caption
        <tr style="border: 2px solid black;">
            <th>Plant Name</th>
            <th>Plant Type</th>
            <th>Quantity</th>
            <th>Price</th>
        </tr>
        """
    for plant in data:
        plant_name = plant[0]
        plant_type = plant[1]
        quantity = plant[2]
        price = plant[3]
        row = f"""<tr style="background-color: #ccffcc;">
            <td>{plant_name}</td>
            <td>{plant_type}</td>
            <td>{quantity}</td>
            <td>{price}</td>
        </tr>"""
    
        info = info + row

    info = info + "</table>"
    return info
    
#basket table browser function
@app.route("/browser_basket_table")
def get_all_basket_data_browser():
    data = get_all_basket_table_data()
    data = data["basket_table"]
    print(data)
    info = f"""

    <table style="background-color:#67c16a;font-family:monospace;font-size:24px;width:100%;border:4px solid black;
  border-collapse:collapse;padding:15px;
  text-align:center;">
        <caption>Basket Table</caption
        <tr style="border: 2px solid black;">
            <th>ID</th>
            <th>Plant Name</th>
            <th>Cart ID</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Created at</th>
            <th>Updated at</th>

        </tr>
        """
    for plant in data:
        id = plant[0]
        plant_name = plant[1]
        cart_id = plant[2]
        price = plant[3]
        quantity = plant[4]
        created_at = plant[5]
        updated_at = plant[6]
        row = f"""<tr style="background-color: #ccffcc;">
            <td>{id}</th>
            <td>{plant_name}</td>
            <td>{cart_id}</td>
            <td>{quantity}</td>
            <td>{price}</td>
            <td>{created_at}</td>
            <td>{updated_at}</td>
        </tr>"""
    
        info = info + row

    info = info + "</table>"
    return info












# plants_data table functions:

@app.route("/plants_data")
def get_all_plants_data():
    # This function is returning all of the plants stock data from the plants_data table in the database.
    conn = db_connect().connect() # connect to database
    query = conn.execute("select * from plants_data") # This line performs query and returns json result
    all_plants_data = [i for i in query.cursor.fetchall()]
    return {'plants_data': all_plants_data} # Fetches the data
    
@app.route("/plants_data/<plant_name>")
def get_single_plant_data(plant_name):
    # When a plant's name is entered into the plant_name input, this function returns all of that plant's data from the plants_data table in the plants_data database.
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


#This function is the add_to_basket1 function before it got finalised. Keeping (uncommented)for now
# @app.route('/plants_data/<plant_name>/<quantity>/<cart_id>')
# def add_to_basket(cart_id, plant_name, quantity):
#     conn = db_connect().connect()
#     price = get_plant_price(plant_name)
#     time_stamp = datetime.datetime.now()
#     query = conn.execute(f"INSERT INTO basket_table (id, plant_name, cart_id, price, quantity, created_at, updated_at) VALUES (1, '{plant_name}', '{cart_id}', '{price}', '{quantity}', '{time_stamp}', 'time');")
#     return f"{plant_name} added to basket"





# basket_table functions:

@app.route('/basket/<plant_name>/<quantity>/<cart_id>')
def add_to_basket1(cart_id, plant_name, quantity):
    # Check if there is already an existing plant with same credentials in basket table
    record = get_record_from_basket_table(cart_id, plant_name)["record"]
    conn = db_connect().connect()
    #checks the quantity and minuses it off. Changing the quantity in the plants_data table.
    #stock/plants_data table
    oldquantity = int(get_plant_quantity(plant_name))
    new_quantity = oldquantity - int(quantity)
    update_quantity(plant_name, new_quantity)
    if len(record) == 0:
        #basket_table data
        price = get_plant_price(plant_name)
        time_stamp = datetime.datetime.now()
        query = conn.execute(f"INSERT INTO basket_table (id, plant_name, cart_id, price, quantity, created_at, updated_at) VALUES (1, '{plant_name}', '{cart_id}', '{price}', '{quantity}', '{time_stamp}', 'time');")
        return f"{plant_name} added to basket"
    oldquantity = record[0][4]
    new_quantity = int(oldquantity) + int(quantity)
    query = conn.execute(f"UPDATE basket_table set quantity = {new_quantity} where cart_id = '{cart_id}' and plant_name = '{plant_name}'")
    return "Basket updated"

#function which will get one basket from the basket_table table
@app.route('/basket/<cart_id>')
def get_basket_from_basket_table(cart_id):
    conn = db_connect().connect() # connect to database
    query = conn.execute(f"select * from basket_table where cart_id='{cart_id}'")
    return {'basket': [i for i in query.cursor]} # Fetches the data

#function which will get one record from the basket_table table
@app.route('/basket/<cart_id>/<plant_name>')
def get_record_from_basket_table(cart_id, plant_name):
    conn = db_connect().connect() # connect to database
    query = conn.execute(f"select * from basket_table where cart_id='{cart_id}' and plant_name='{plant_name}'")
    return {'record': [i for i in query.cursor]} # Fetches the data

#function which will remove one record from the basket_table table
def remove_record_from_basket_table(cart_id):
    conn = db_connect().connect()
    basket_record = get_basket_from_basket_table(cart_id)['record']
    # import pytest
    # pytest.set_trace()
    # print(basket_record)
    for plant in basket_record:
        basket_quantity = plant[4]
        plant_name = plant[1]
        # old quantity of the stock from the plants_data table to know what to change it back to
        oldquantity = int(get_plant_quantity(plant_name))
        update_quantity(plant_name, oldquantity + basket_quantity)
    query = conn.execute(f"delete from basket_table where cart_id='{cart_id}'")



@app.route("/basket_table_data")
def get_all_basket_table_data():
    # This function is returning all of the plants stock data from the basket_table table in the database.
    conn = db_connect().connect() # connect to database
    query = conn.execute("select * from basket_table") # This line performs query and returns json result
    all_plants_data = [i for i in query.cursor.fetchall()]
    return {'basket_table': all_plants_data} # Fetches the data


# NEED TO MAKE A TEST FOR THIS!
@app.route("/basket_table_data/all_items_quantity")
def get_basket_table_quantity():
    #This function returns the quantity of all items in the basket database
    conn = db_connect().connect()
    query = conn.execute("select quantity from basket_table")
    jsonQuantities = [i for i in query.cursor]
    basketQuantity = 0
    for quantity in jsonQuantities:
        basketQuantity = basketQuantity + quantity[0]
    return str(basketQuantity)



if __name__ == '__main__':
     app.run(port='5002')