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
def test_print_entire_table():
    db = Database()
    users = db.get_all_records_any_table("products")

    print(users)


 # test #4
@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1" # values stored as a list, first row is 0, then goes columns.
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"

 # test #5 
@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25) # updating quantity
    water_qnt = db.select_product_qnt_by_id(1) # get the quantity of the item

    assert water_qnt[0][0] == 25 # verifies that quantity equal to the value that we provided


 # test #6
@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    cookie_qnt = db.select_product_qnt_by_id(4)

    assert cookie_qnt[0][0] == 30 


 # tests #7
@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'data', 999) # create temp test data in the table
    db.delete_product_by_id(99) # delete temp test data from the table
    qnt = db.select_product_qnt_by_id(99) # verify that created test data is deleted

    assert len(qnt) == 0 # confirm that test data doesn't exist in the table


 # test #8
@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Orders details:", orders)
    # check quantity of orders equal to 1
    assert len(orders) == 6

    # check structure ord data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


 # test #9
@pytest.mark.database    
def test_order_insert():
    db = Database()
    db.insert_order(6, 2, 1, "14:02:47")
    cust_id = db.select_last_order()

    assert cust_id[0][1] == "14:02:47"


 # test #10
@pytest.mark.database    
def test_get_order_by_id():
    db = Database()
    order = db.select_order_by_id(2)

    assert order [0][1] == "12:28:03"


 # test #11
@pytest.mark.database
def test_check_last_order():
    db = Database()
    last_order = db.select_last_order()

    assert last_order [0][1] == "14:02:47"


 # test #12
@pytest.mark.database
def test_get_order_date_after_specific_time_point():
    db = Database()
    orders = db.select_specific_range_order_date_for_users("13:10:00")

    #print(orders)
    assert orders[0][2] >= "13:10:00"


 # test #13
@pytest.mark.database
def test_product_qnt_update_with_wrong_value_type():  
    # negative test to verify that int can not by updated by str
    db = Database()
    db.negative_update_product_qnt_by_id_using_str(1, "A") # updating quantity
    water_qnt = db.select_product_qnt_by_id(1) # get the quantity of the item

    print(water_qnt)

    assert water_qnt[0][0] == "A" # verifies that quantity equal to the value that we provided


 # test #14
@pytest.mark.database
def test_check_data_type_of_value_in_qnt_column(): 
    db = Database()
    quantity_value = db.select_product_qnt_by_id(1)
    data_type = quantity_value[0][0]
    
    #print(data_type)
    print(type(data_type))
    assert isinstance(data_type, int) # The data type of the quantity value is checked using the 'isinstance' 
