

class Products:
    def __init__(self, name, category, price, stock_quantity):
        self.name = name
        self.category = category
        self.stock_quantity = stock_quantity
        self.price = price

    def __str__(self):
        return f"Product Name: {self.name} Category: {self.category} Stock: {self.stock_quantity} Price{self.price}"
