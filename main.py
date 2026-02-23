import products
import store


def start(best_buy):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        # Option 1: list products
        if choice == "1":
            all_products = best_buy.get_all_products()
            if not all_products:
                print("No active products in store.")
            else:
                for i, product in enumerate(all_products, start=1):
                    print(f"{i}. ", end="")
                    product.show()

        # Option 2: show total quantity
        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")

        # Option 3: make an order
        elif choice == "3":
            all_products = best_buy.get_all_products()
            if not all_products:
                print("No active products available to order.")
                continue

            shopping_list = []

            while True:
                print("\nAvailable products:")
                for i, product in enumerate(all_products, start=1):
                    print(f"{i}. ", end="")
                    product.show()

                selection = input(
                    "Enter product number to add (or press Enter to finish): "
                ).strip()

                if selection == "":
                    break

                try:
                    product_index = int(selection)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if product_index < 1 or product_index > len(all_products):
                    print("That product number is not in the list.")
                    continue

                qty_str = input("Enter quantity: ").strip()
                try:
                    qty = int(qty_str)
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")
                    continue

                shopping_list.append((all_products[product_index - 1], qty))

            if not shopping_list:
                print("No items ordered.")
                continue

            try:
                total_cost = best_buy.order(shopping_list)
                print(f"Order cost: {total_cost} dollars.")
            except Exception as e:
                print(f"Order failed: {e}")

        # Option 4: quit
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
