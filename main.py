from store_inventory import Store
from product import Products


def display_menu():
    print("Welcome to My Store")
    print("1. Add product")
    print("2. View products")
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
        elif command == "2":
            inventory.view_products()
        elif command == "3":

            print("choose column you want to update")
            print(" 1. product name")
            print(" 2. product category")
            print(" 3. product quantity")
            print(" 4. product price")

            option = input("enter column to update value: ")

            match option:

                case "1":
                    product_n = input("Enter product name to update: ")
                    product_name = input("Enter new Name: ")
                    inventory.update_product(product_n, product_name)
                case "2":
                    product_name = input("Enter product name to update: ")
                    category = input("Enter new category: ")
                    inventory.update_category(product_name, category)
                case "3":
                    product_id = int(input("Enter product ID to update: "))
                    quantity = int(input("Enter new quantity: "))
                    inventory.update_stock(product_id, quantity)
                case "4":
                    product_name = input("Enter product name to update: ")
                    price = float(input("Enter new price: "))
                    inventory.update_price(product_name, price)
                case _:
                    print("Invalid column")


if __name__ == "__main__":
    main()
