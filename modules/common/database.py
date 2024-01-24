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


    def get_all_records_any_table(self, t_name):
        query = f"SELECT * FROM '{t_name}'"
        self.cursor.execute(query) # execute query in db
        record = self.cursor.fetchall() # save the result of the query
        return record

    
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
    

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
        VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit() # confirmation of changes in db to prevent any updates by mistake


    def insert_order(self, id, customer_id, product_id, order_date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
        VALUES ({id}, '{customer_id}', '{product_id}', '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()

    
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name,  \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall() # save result of the query in record variable
        return record
    
    def select_order_by_id(self, id):
        query = f"SELECT id, order_date FROM orders WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall() # save the result of the query
        return record
    

    def select_last_order(self):
        query = f"SELECT id, order_date FROM orders \
            ORDER by id DESC \
            LIMIT 1"
        self.cursor.execute(query)
        last_order = self.cursor.fetchall() # save the result of the query

        return last_order