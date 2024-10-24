class Products:
    def __init__(self, name, category, stock_quantity, price):
        self.name = name
        self.category = category
        self.stock_quantity = stock_quantity
        self.price = price

    def __str__(self):
        return f"{self.name} in {self.category} remaining {self.stock_quantity} sold at {self.price}"
