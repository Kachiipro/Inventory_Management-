from product import Products
from dbconn import Database


class Store:
    def __init__(self):
        self.db = Database()

    def add_product(self, products):
        query = "INSERT INTO My_Inventory (product_name, product_category, product_quantity, product_price ) VALUES (%s, %s,%s, %s)"
        self.db.execute_q(query, (products.name, products.category,
                          products.price, products.stock_quantity))
        print(f"Product '{products.name}' added successfully.")

    def view_products(self):
        query = "SELECT * FROM My_Inventory"
        products = self.db.fetch_q(query)
        if products:
            for p in products:
                print(p)
        else:
            print("no product In inventory")

    def update_product(self, product_n, product_name):
        query = "UPDATE My_Inventory SET product_name = %s WHERE product_name = %s "
        self.db.execute_q(query, (product_name, product_n))
        print("update succesfull")

    def update_stock(self, product_id, quantity):
        query = "UPDATE My_Inventory SET product_quantity = %s WHERE product_id = %s"
        self.db.execute_q(query, (quantity, product_id))
        print(f"Product ID {product_id} updated to quantity {quantity}.")

    def update_category(self, product_n, category):
        query = "UPDATE My_Inventory SET product_category = %s WHERE product_name = %s "
        self.db.execute_q(query, (category, product_n))
        print("update succesfull")

    def update_price(self, product_n, price):
        query = "UPDATE My_Inventory SET product_price = %s WHERE product_name = %s "
        self.db.execute_q(query, (price, product_n))
        print("update succesfull")
