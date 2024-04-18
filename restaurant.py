import time
import json
from menu import Menu  # Assuming Menu class is defined in menu.py

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
        print("What would you like to have today?\n")
        print("╔════════════════════════════════════════════════╗")
        print("║                  Main Menu                     ║")
        print("╠════════════════════════════════════════════════╣")
        menu_items = self.menu.get_menu_items()
        for num, category in enumerate(menu_items, start=1):
            if num < 10:
                print(f"║    {num}. {category:<41}║")
            else:
                print(f"║   {num}. {category:<41}║")
        print("║   13. Exit                                     ║")
        print("╚════════════════════════════════════════════════╝")

    def handle_choice(self, choice):
        try:
            choice = int(choice)
            menu_items = list(self.menu.get_menu_items().keys())
            if choice == 13:
                print("\nGoodbye! Have a great day!")
                return False
            selected_category = menu_items[choice - 1]
            self.display_category(selected_category)
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

    def display_category(self, category):
        print(f"\n{category}:")
        items = self.menu.get_menu_items()[category]
        if items:
            print("-" * 215)
            print("{:<5} | {:<40} | {:<150} | {:<10}".format("No.", "Item", "Description", "Price (RWF)"))
            print("-" * 215)
            for index, item in enumerate(items, start=1):
                item_name = item["name"][:35] + "..." if len(item["name"]) > 35 else item["name"]
                description = item["description"][:150] + "..." if len(item["description"]) > 150 else item["description"]
                print("{:<5} | {:<40} | {:<150} | {:<10}".format(index, item_name, description, item["price"]))
            print("-" * 215)
            self.place_order(category)
        else:
            print("No items available in this category.")
            input("\nPress Enter to return to the main menu...")

    def place_order(self, category):
        with open(self.orders_file, "a") as file:
            while True:
                choice = input("\nEnter the number of the item you want to order (e.g., '1' for the first item, 'back' to return to main menu): ")
                if choice.lower() == 'back':
                    self.display_menu()
                    choice = input("\nEnter your choice (1-13): ")
                    if not self.handle_choice(choice):
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

    def main(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-13): ")
            if not self.handle_choice(choice):
                break

if __name__ == "__main__":
    username = input("Welcome! Please enter your username: ")
    restaurant = Restaurant(username)
    restaurant.main()
