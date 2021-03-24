import mock
import pytest
from freezegun import freeze_time
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from rest_api import get_all_plants_data
from rest_api import get_single_plant_data
from rest_api import get_plant_price
from rest_api import get_plant_quantity
from rest_api import single_plant_bought
from rest_api import update_stock_quantity
from rest_api import db_connect
from rest_api import add_to_basket1
from rest_api import get_basket_from_basket_table
from rest_api import remove_record_from_basket_table
from rest_api import get_all_basket_table_data
from rest_api import get_record_from_basket_table
from rest_api import remove_one_item_from_basket_table
from rest_api import get_basket_table_quantity
from rest_api import get_single_plant_data_browser
from rest_api import get_all_plant_data_browser
from rest_api import get_all_basket_data_browser
from rest_api import restore_quantities_plants_data
from rest_api import restore_basket_table_to_zero


db_connect = create_engine('sqlite:///tests/database/test_plants_database.db')

# plants_data tests

# @mock.patch("rest_api.db_connect")
# def test_get_all_plants_data(mock_db_connect):
#     mock_db_connect.return_value = db_connect
#     response = get_all_plants_data()
#     assert response == {'plants_data': [('Bonsai', 'Indoor', 500, 20), ('Peace Lily', 'Indoor', 500, 20)]}

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

# @freeze_time("2020-04-11")
# @mock.patch("rest_api.db_connect")
# def test_get_all_basket_table_data(mock_db_connect):
#     mock_db_connect.return_value = db_connect
#     # Add an item to the basket
#     add_to_basket1('test_cart_id1', 'Bonsai', 1)
#     add_to_basket1('test_cart_id2', 'Peace Lily', 1)
#     response = get_all_basket_table_data()
#     assert response ==  {'basket_table': [('1', 'Bonsai', 'test_cart_id1', 20, 1, '2020-04-11 00:00:00', 'time'), ('1', 'Peace Lily', 'test_cart_id2', 20, 1, '2020-04-11 00:00:00', 'time')]}
#     # Remove record
#     remove_record_from_basket_table('test_cart_id1')
#     remove_record_from_basket_table('test_cart_id2')



# @freeze_time("2020-04-11")
# @mock.patch("rest_api.db_connect")
# def test_get_record_from_basket_table(mock_db_connect):
#     mock_db_connect.return_value = db_connect
#     #add item to basket
#     add_to_basket1('test_cart_id1', 'Bonsai', 1)
#     response = get_record_from_basket_table('test_cart_id1', 'Bonsai')
#     assert response == {'record': [('1', 'Bonsai', 'test_cart_id1', 20, 1, '2020-04-11 00:00:00', 'time')]}
#     remove_record_from_basket_table('test_cart_id1')

# @freeze_time("2020-04-11")
# @mock.patch("rest_api.db_connect")
# def test_remove_one_item_from_basket_table(mock_db_connect):
#     mock_db_connect.return_value = db_connect
#     add_to_basket1('test_cart_id1', 'Bonsai', 1)
#     # we need to make sure that the item gets added and removed so we should store what is currently in basket and then show that it is no longer there
    
#     old_stock_quantity = get_plant_quantity('Bonsai')
    
#     remove_one_item_from_basket_table('test_cart_id1', 'Bonsai')
#     new_stock_quantity = get_plant_quantity('Bonsai')
   
#     assert get_basket_from_basket_table('test_cart_id1') == {'basket': []}
#     assert int(new_stock_quantity) == int(old_stock_quantity) + 1


# @freeze_time("2020-04-11")
# @mock.patch("rest_api.db_connect")
# def test_get_basket_table_quantity(mock_db_connect):
#     mock_db_connect.return_value = db_connect
#     add_to_basket1('test_cart_id1', 'Bonsai', 2)
#     add_to_basket1('test_cart_id1', 'Peace Lily', 1)
#     response = get_basket_table_quantity()
#     assert response == '3'
#     remove_record_from_basket_table('test_cart_id1')



# Browser JSON to HTML tests

@mock.patch("rest_api.db_connect")
def test_get_single_plant_data_browser(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_single_plant_data_browser('Bonsai')
    assert bool(BeautifulSoup(response, "html.parser").find()) == True

@mock.patch("rest_api.db_connect")
def test_get_all_plant_data_browser(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_all_plant_data_browser()
    assert bool(BeautifulSoup(response, "html.parser").find()) == True

@mock.patch("rest_api.db_connect")
def test_get_all_basket_data_browser(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_all_basket_data_browser()
    assert bool(BeautifulSoup(response, "html.parser").find()) == True


# # restore quantities tests
# # plants data
@mock.patch("rest_api.db_connect")
def test_restore_quantities_plants_data(mock_db_connect):
    mock_db_connect.return_value = db_connect
    old_stock_quantity = get_plant_quantity('Peace Lily')
    response = restore_quantities_plants_data()
    new_stock_quantity = get_plant_quantity('Peace Lily')
    assert int(new_stock_quantity) + 400 == int(old_stock_quantity)
    assert response == "all quantity updated to 100"
    update_stock_quantity('Peace Lily', 500)
    update_stock_quantity('Bonsai', 500)


#basket table

# NEED TO FINISH THIS!!!

@mock.patch("rest_api.db_connect")
def test_restore_basket_table_to_zero(mock_db_connect):
    mock_db_connect.return_value = db_connect
    add_to_basket1('cartid', 'Peace Lily', 6)
    old_basket_quantity = get_basket_table_quantity()
    print(old_basket_quantity)
    response = restore_basket_table_to_zero()
    new_basket_quantity = get_basket_table_quantity()
    print(new_basket_quantity)
    assert int(old_basket_quantity) - 6 == int(new_basket_quantity)
    assert response == "all quantity updated to 0"
    update_stock_quantity('Peace Lily', 500)
