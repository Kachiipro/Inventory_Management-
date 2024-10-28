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
