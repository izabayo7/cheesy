import time
import json

class Restaurant:
    def __init__(self):
        self.menu = {
            1: "Cold Starters",
            2: "Hot Starters",
            3: "Snacks",
            4: "Beefs",
            5: "Chickens",
            6: "Fish",
            7: "Pastas",
            8: "Vegetarians",
            9: "Health Foods",
            10: "Pizzas",
            11: "Grilled",
            12: "Desserts"
        }
        self.menu_items = {
            "Cold Starters": [],
            "Hot Starters": [],
            "Snacks": [],
            "Beefs": [],
            "Chickens": [],
            "Fish": [],
            "Pastas": [],
            "Vegetarians": [],
            "Health Foods": [],
            "Pizzas": [],
            "Grilled": [],
            "Desserts": []
        }
        self.user = self.get_username()
        self.orders_file = f"{self.user}_orders.txt"
        self.populate_menu()

    def get_username(self):
        username = input("Welcome! Please enter your username: ")
        return username

    def load(self):
        print("Starting App", end="")
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(0.1)
        print("100%\n")

    def populate_menu(self):
        # Add menu items for each category
        self.menu_items["Cold Starters"] = [
            {"name": "Caesar Salad", "description": "Romaine lettuce with croutons, parmesan cheese, and Caesar dressing.", "price": "1500"},
            {"name": "Caprese Salad", "description": "Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.", "price": "1800"},
            {"name": "Shrimp Cocktail", "description": "Chilled shrimp served with cocktail sauce and lemon wedges.", "price": "2500"},
            {"name": "Bruschetta", "description": "Toasted bread topped with diced tomatoes, garlic, basil, and balsamic glaze.", "price": "1200"}
        ]

        self.menu_items["Hot Starters"] = [
            {"name": "Garlic Bread", "description": "Toasted bread with garlic butter.", "price": "800"},
            {"name": "Spinach Artichoke Dip", "description": "Creamy dip with spinach, artichokes, and cheese, served with tortilla chips.", "price": "1200"},
            {"name": "Stuffed Mushrooms", "description": "Mushroom caps filled with seasoned breadcrumbs and cheese.", "price": "1500"}
        ]

        self.menu_items["Snacks"] = [
            {"name": "Chicken Wings", "description": "Crispy chicken wings tossed in buffalo sauce, served with ranch dressing.", "price": "2000"},
            {"name": "Loaded Nachos", "description": "Tortilla chips topped with cheese, jalapeños, sour cream, and guacamole.", "price": "1800"},
            {"name": "Mozzarella Sticks", "description": "Breaded and fried mozzarella sticks, served with marinara sauce.", "price": "1600"}
        ]

        self.menu_items["Beefs"] = [
            {"name": "Beef Burger", "description": "Grilled beef patty with lettuce, tomato, onion, and pickles, served with fries.", "price": "2500"},
            {"name": "Beef Steak", "description": "Juicy grilled beef steak served with mashed potatoes.", "price": "3500"},
            {"name": "Beef Tacos", "description": "Soft tortillas filled with seasoned beef, lettuce, cheese, and salsa.", "price": "1800"}
        ]

        self.menu_items["Chickens"] = [
            {"name": "Roast Chicken", "description": "Roasted chicken with herbs and spices, served with roasted vegetables.", "price": "2800"},
            {"name": "Chicken Alfredo", "description": "Grilled chicken breast with creamy Alfredo sauce over fettuccine pasta.", "price": "3200"},
            {"name": "Chicken Quesadilla", "description": "Grilled flour tortilla filled with chicken, cheese, and bell peppers.", "price": "1800"}
        ]

        # Add more menu items for other categories...

    def display_menu(self):
        print("\n\n*******************************************************")
        print("****************** WELCOME TO CHEESY *****************")
        print("*******************************************************\n")
        print(f"Hello, {self.user}! What would you like to have today?\n")
        for num, category in self.menu.items():
            print(f"{num}. {category}")

    def handle_choice(self, choice):
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(self.menu):
                selected_category = self.menu[choice]
                self.display_category(selected_category)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

    def display_category(self, category):
        print(f"\n{category}:")
        items = self.menu_items[category]
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
        choice = input("\nEnter the number of the item you want to order (e.g., '1' for the first item, 'back' to return to main menu): ")
        if choice.lower() == 'back':
            self.return_to_main_menu()
        else:
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.menu_items[category]):
                    selected_item = self.menu_items[category][choice - 1]
                    self.save_order(selected_item)
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def save_order(self, item):
        order_data = {
            "item": item["name"],
            "description": item["description"],
            "price": item["price"]
        }
        with open(self.orders_file, "a") as file:
            file.write(json.dumps(order_data) + "\n")
        print("Order placed successfully!")

    def return_to_main_menu(self):
        print("\nReturning to the main menu...\n")

    def main(self):
        self.load()
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-12, 'exit' to quit): ")
            if choice.lower() == 'exit':
                break
            self.handle_choice(choice)

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.main()
