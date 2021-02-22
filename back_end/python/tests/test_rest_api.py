import mock
import pytest
from freezegun import freeze_time
from sqlalchemy import create_engine
from rest_api import get_all_plants_data
from rest_api import get_single_plant_data
from rest_api import get_plant_price
from rest_api import get_plant_quantity
from rest_api import single_plant_bought
from rest_api import update_quantity
from rest_api import db_connect
from rest_api import add_to_basket
from rest_api import add_to_basket1
from rest_api import get_record_from_basket_table
from rest_api import remove_record_from_basket_table

db_connect = create_engine('sqlite:///tests/database/test_plants_database.db')

@mock.patch("rest_api.db_connect")
def test_get_all_plants_data(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_all_plants_data()
    assert response == {'plants_data': [('Bonsai', 'Indoor', 3, 20), ('Peace Lily', 'Indoor', 7, 20)]}

@mock.patch("rest_api.db_connect")
def test_get_single_plant_data(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_single_plant_data('Bonsai')
    assert response == {'record': [('Bonsai', 'Indoor', 3, 20)]}

@mock.patch("rest_api.db_connect")
def test_get_plant_price(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_plant_price('Bonsai')
    assert response == '20'

@mock.patch("rest_api.db_connect")
def test_get_plant_quantity(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_plant_quantity('Bonsai')
    assert response == '3'

@mock.patch("rest_api.db_connect")
def test_single_plant_bought(mock_db_connect):
    mock_db_connect.return_value = db_connect
    old_quantity = get_plant_quantity('Bonsai')
    
    single_plant_bought('Bonsai')
    new_quantity = get_plant_quantity('Bonsai') 
    assert int(new_quantity) == int(old_quantity) - 1

    update_quantity('Bonsai', old_quantity)


@mock.patch("rest_api.db_connect")
def test_update_quantity(mock_db_connect):
    mock_db_connect.return_value = db_connect
    old_quantity = get_plant_quantity('Bonsai')
    update_quantity('Bonsai', 50)
    new_quantity = get_plant_quantity('Bonsai')
    assert int(new_quantity) == 50
    update_quantity('Bonsai', old_quantity)

# @freeze_time("2020-04-11")
# @mock.patch("rest_api.db_connect")
# def test_add_to_basket(mock_db_connect):
#     mock_db_connect.return_value = db_connect
#     add_to_basket('test_cart_id', 'Bonsai', 1)
#     response = get_record_from_basket_table('test_cart_id')
#     assert response == {'record': [('1', 'Bonsai', 'test_cart_id', 20, 1, '2020-04-11 00:00:00', 'time')]}
#     remove_record_from_basket_table('test_cart_id')

@freeze_time("2020-04-11")
@mock.patch("rest_api.db_connect")
def test_add_to_basket1(mock_db_connect):
    mock_db_connect.return_value = db_connect
    #stock
    oldstockquantity = int(get_plant_quantity('Bonsai'))
    #call the add to basket function
    add_to_basket1('test_cart_id', 'Bonsai', 1)
    newstockquantity = int(get_plant_quantity('Bonsai'))
    assert oldstockquantity - newstockquantity == 1
    #basket
    response = get_record_from_basket_table('test_cart_id')
    assert response == {'record': [('1', 'Bonsai', 'test_cart_id', 20, 1, '2020-04-11 00:00:00', 'time')]}
    remove_record_from_basket_table('test_cart_id')
    update_quantity('Bonsai', oldstockquantity)


@mock.patch("rest_api.db_connect")
def test_get_record_from_basket_table(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_record_from_basket_table('abc')
    assert response == {'record': [('1', 'Bonsai', 'abc', 20, 1, '2021-02-17 16:17:15.871149', 'time')]}
    
@mock.patch("rest_api.db_connect")
def test_remove_record_from_basket_table(mock_db_connect):
    mock_db_connect.return_value = db_connect
    
    add_to_basket('test_cart_id', 'Peace Lily', 1)
    
    remove_record_from_basket_table('test_cart_id')
    
    assert get_record_from_basket_table('test_cart_id') == {'record': []}

