import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect("D:\\QA\\Repo\\GitHub_automation_testing" + r"\\become_qa_auto.db") # it creates interaction with db
        self.cursor = self.connection.cursor() # performs the commands in db
 

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();" #print out current db version
        self.cursor.execute(sqlite_select_Query) # executes query in db
        record = self.cursor.fetchall() # get result of the query
        print(f"Connected succesfully. SQLite Database Version is: {record}")

    
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query) # execute query in db
        record = self.cursor.fetchall() # save the result of the query
        return record
    

    def get_user_address_by_name(self, name): 
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall() # save the result of the query
        return record
    

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit() # confirmation of changes in db to prevent any updates by mistake

    
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall() # save the result of the query 
        return record
    

    


    