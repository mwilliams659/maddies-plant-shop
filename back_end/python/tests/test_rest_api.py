import mock
import pytest
from freezegun import freeze_time
from sqlalchemy import create_engine
from rest_api import get_all_plants_data
from rest_api import get_single_plant_data
from rest_api import get_plant_price
from rest_api import get_plant_quantity
from rest_api import single_plant_bought
from rest_api import update_stock_quantity
from rest_api import db_connect
# from rest_api import add_to_basket
from rest_api import add_to_basket1
from rest_api import get_basket_from_basket_table
from rest_api import remove_record_from_basket_table
from rest_api import get_all_basket_table_data

db_connect = create_engine('sqlite:///tests/database/test_plants_database.db')

# plants_data tests

@mock.patch("rest_api.db_connect")
def test_get_all_plants_data(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_all_plants_data()
    assert response == {'plants_data': [('Bonsai', 'Indoor', 500, 20), ('Peace Lily', 'Indoor', 500, 20)]}

@mock.patch("rest_api.db_connect")
def test_get_single_plant_data(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_single_plant_data('Bonsai')
    assert response == {'record': [('Bonsai', 'Indoor', 500, 20)]}

@mock.patch("rest_api.db_connect")
def test_get_plant_price(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_plant_price('Bonsai')
    assert response == '20'

@mock.patch("rest_api.db_connect")
def test_get_plant_quantity(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_plant_quantity('Bonsai')
    assert response == '500'

@mock.patch("rest_api.db_connect")
def test_single_plant_bought(mock_db_connect):
    mock_db_connect.return_value = db_connect
    old_quantity = get_plant_quantity('Bonsai')
    
    single_plant_bought('Bonsai')
    new_quantity = get_plant_quantity('Bonsai') 
    assert int(new_quantity) == int(old_quantity) - 1

    update_stock_quantity('Bonsai', old_quantity)


@mock.patch("rest_api.db_connect")
def test_update_stock_quantity(mock_db_connect):
    mock_db_connect.return_value = db_connect
    old_quantity = get_plant_quantity('Bonsai')
    update_stock_quantity('Bonsai', 50)
    new_quantity = get_plant_quantity('Bonsai')
    assert int(new_quantity) == 50
    update_stock_quantity('Bonsai', old_quantity)


#basket_table tests:

@freeze_time("2020-04-11")
@mock.patch("rest_api.db_connect")
def test_add_to_basket1(mock_db_connect):
    mock_db_connect.return_value = db_connect
    #stock
    oldstockquantity = int(get_plant_quantity('Bonsai'))
    #call the add to basket function
    add_to_basket1('test_cart_id1', 'Bonsai', 1)
    newstockquantity = int(get_plant_quantity('Bonsai'))
    assert oldstockquantity - newstockquantity == 1
    #basket
    response = get_basket_from_basket_table('test_cart_id1')
    assert response == {'basket': [('1', 'Bonsai', 'test_cart_id1', 20, 1, '2020-04-11 00:00:00', 'time')]}
    remove_record_from_basket_table('test_cart_id1')
    update_stock_quantity('Bonsai', oldstockquantity)

@freeze_time("2020-04-11")
@mock.patch("rest_api.db_connect")
def test_get_basket_from_basket_table(mock_db_connect):
    mock_db_connect.return_value = db_connect
    # Add an item to the basket
    add_to_basket1('test_cart_id1', 'Bonsai', 1)
    # Add an extra basket item to the basket to show it only gets the first basket
    add_to_basket1('test_cart_id2', 'Peace Lily', 1)
    response = get_basket_from_basket_table('test_cart_id1')
    assert response == {'basket': [('1', 'Bonsai', 'test_cart_id1', 20, 1, '2020-04-11 00:00:00', 'time')]}
    remove_record_from_basket_table('test_cart_id1')
    remove_record_from_basket_table('test_cart_id2')
    
@mock.patch("rest_api.db_connect")
def test_remove_record_from_basket_table(mock_db_connect):
    mock_db_connect.return_value = db_connect
    add_to_basket1('test_cart_id1', 'Peace Lily', 1)
    
    old_stock_quantity = get_plant_quantity('Peace Lily')
    
    remove_record_from_basket_table('test_cart_id1')
    new_stock_quantity = get_plant_quantity('Peace Lily')
   
    assert get_basket_from_basket_table('test_cart_id1') == {'basket': []}
    assert int(new_stock_quantity) == int(old_stock_quantity) + 1

@freeze_time("2020-04-11")
@mock.patch("rest_api.db_connect")
def test_get_all_basket_table_data(mock_db_connect):
    mock_db_connect.return_value = db_connect
    # Add an item to the basket
    add_to_basket1('test_cart_id1', 'Bonsai', 1)
    add_to_basket1('test_cart_id2', 'Peace Lily', 1)
    response = get_all_basket_table_data()
    assert response ==  {'basket_table': [('1', 'Bonsai', 'test_cart_id1', 20, 1, '2020-04-11 00:00:00', 'time'), ('1', 'Peace Lily', 'test_cart_id2', 20, 1, '2020-04-11 00:00:00', 'time')]}
    # Remove record
    remove_record_from_basket_table('test_cart_id1')
    remove_record_from_basket_table('test_cart_id2')