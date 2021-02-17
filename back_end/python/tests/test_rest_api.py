import mock
import pytest
from sqlalchemy import create_engine
from rest_api import get_all_plants_data
from rest_api import get_single_plant_data
from rest_api import get_plant_quantity
from rest_api import single_plant_bought
from rest_api import update_quantity
from rest_api import db_connect
from rest_api import add_to_basket
from rest_api import get_record_from_basket_table

db_connect = create_engine('sqlite:///tests/database/test_plants_database.db')
cart_id = 'abc'

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

# @mock.patch("rest_api.db_connect")
# def test_add_to_basket(mock_db_connect):
#     cart_id = 'abc'
#     plant_name = 'Bonsai'
#     quantity = 1
#     price = 20
#     mock_db_connect.return_value = db_connect
#     response = add_to_basket(cart_id, plant_name, quantity, price)
#     assert response == 'abc'

@mock.patch("rest_api.db_connect")
def test_get_record_from_basket_table(mock_db_connect):
    mock_db_connect.return_value = db_connect
    response = get_record_from_basket_table(cart_id)
    assert response == {'record': [('1', 'Bonsai', 'abc', 20, 1, '2021-02-17 16:17:15.871149', 'time')]}
    