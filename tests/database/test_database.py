import pytest
from modules.common.database import Database # import class - Database to work with db

 # test #1
@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

 # test #2
@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print (users)

 # test #3
@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")
    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


 # test #4 
@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25) # updating quantity
    water_qnt = db.select_product_qnt_by_id(1) # get the quantity of the item
    assert water_qnt[0][0] == 25 # verifies that quantity equal to the value that we provided


    

    