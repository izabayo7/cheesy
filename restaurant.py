# restaurant.py

import time
import json
from menu import Menu

class Restaurant:
    def __init__(self, username):
        self.user = username
        self.orders_file = f"{self.user}_orders.txt"
        self.menu = Menu()
        self.load()

    def load(self):
        print("Starting App", end="")
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(0.1)
        print("100%\n")

    def display_menu(self):
        print("\n\n*******************************************************")
        print("****************** WELCOME TO CHEESY *****************")
        print("*******************************************************\n")
        print(f"Hello, {self.user}! What would you like to have today?\n")
        menu_items = self.menu.get_menu_items()
        for num, category in enumerate(menu_items, start=1):
            print(f"{num}. {category}")

    def handle_choice(self, choice):
        try:
            choice = int(choice)
            menu_items = list(self.menu.get_menu_items().keys())
            selected_category = menu_items[choice - 1]
            self.display_category(selected_category)
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

    def display_category(self, category):
        print(f"\n{category}:")
        items = self.menu.get_menu_items()[category]
        if items:
            print("{:<5} | {:<30} | {:<60} | {:<10}".format("No.", "Item", "Description", "Price (RWF)"))
            print("-" * 125)
            for index, item in enumerate(items, start=1):
                print("{:<5} | {:<30} | {:<60} | {:<10}".format(index, item["name"], item["description"], item["price"]))
            print("-" * 125)
            self.place_order(category)
        else:
            print("No items available in this category.")
            self.return_to_main_menu()

    def place_order(self, category):
        with open(self.orders_file, "a") as file:
            while True:
                choice = input("\nEnter the number of the item you want to order (e.g., '1' for the first item, 'back' to return to main menu): ")
                if choice.lower() == 'back':
                    self.return_to_main_menu()
                    break
                try:
                    choice = int(choice)
                    items = self.menu.get_menu_items()[category]
                    if 1 <= choice <= len(items):
                        selected_item = items[choice - 1]
                        order_data = {
                            "item": selected_item["name"],
                            "description": selected_item["description"],
                            "price": selected_item["price"]
                        }
                        file.write(json.dumps(order_data) + "\n")
                        print("Order placed successfully!")
                    else:
                        print("Invalid item number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def return_to_main_menu(self):
        print("\nReturning to the main menu...\n")

    def main(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-12, 'exit' to quit): ")
            if choice.lower() == 'exit':
                break
            self.handle_choice(choice)

if __name__ == "__main__":
    username = input("Welcome! Please enter your username: ")
    restaurant = Restaurant(username)
    restaurant.main()
