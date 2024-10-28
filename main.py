from store_inventory import Store
from product import Products


def display_menu():
    print("Welcome to My Store")
    print("1. Add product")
    print("2. Track Stock")
    print("3. Update product details and stock quantities.")
    print("4. Search and sort products")
    print("5. Exit")
    print()


def main():
    inventory = Store()
    while True:
        display_menu()
        command = input("Select Option 1-5: ")
        if command == "1":
            print("Add new product")
            name = input("Enter Product Name: ")
            category = input("Product Category: ")
            stock_quantity = input("Quantity: ")
            price = input("Product Price: ")
            products = Products(name, category, stock_quantity, price)
            inventory.add_product(products)


if __name__ == "__main__":
    main()
