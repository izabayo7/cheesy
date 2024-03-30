import time

# Function for application loader
def load():
    print("Starting App", end="")
    for _ in range(10):
        print(".", end="", flush=True)
        time.sleep(0.1)
    print("100%\n")

# Function to display the restaurant menu
def display_menu():
    print("\n\n*******************************************************")
    print("****************** WELCOME TO CHEESY *****************")
    print("*******************************************************\n")
    print("What would you like to have today?\n")
    print("╔═══════════════════════════════════════════════════╗")
    print("║                  Main Menu                        ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║    1. Appetizers                                  ║")
    print("║    2. Main Courses                                ║")
    print("║    3. Desserts                                    ║")
    print("║    4. Beverages                                   ║")
    print("║    5. Specials                                    ║")
    print("║    6. Vegetarian Options                          ║")
    print("║    7. Exit                                        ║")
    print("╚═══════════════════════════════════════════════════╝")

# Function to handle user's choice
def handle_choice(choice):
    if choice == '1':
        display_appetizers()
    elif choice == '2':
        display_main_courses()
    elif choice == '3':
        display_desserts()
    elif choice == '4':
        display_beverages()
    elif choice == '5':
        display_specials()
    elif choice == '6':
        display_vegetarian_options()
    elif choice == '7':
        exit_program()
    else:
        print("Invalid choice. Please try again.")

# Function to display appetizers in tabular format
def display_appetizers():
    print("\nAppetizers:")
    print("{:<5} | {:<20} | {:<90} | {:<10}".format("No.", "Appetizer", "Description", "Price (RWF)"))
    print("-" * 125)
    appetizers = [
        {"name": "Garlic Bread", "description": "Freshly baked bread with garlic butter.", "price": "1000"},
        {"name": "Bruschetta", "description": "Toasted bread topped with diced tomatoes, garlic, basil, and balsamic glaze.", "price": "1500"},
        {"name": "Mozzarella Sticks", "description": "Breaded and fried mozzarella cheese sticks served with marinara sauce.", "price": "2000"},
        {"name": "Onion Rings", "description": "Crispy battered onion rings served with a dipping sauce.", "price": "1800"},
        {"name": "Caprese Salad", "description": "Fresh mozzarella, tomatoes, basil, olive oil, and balsamic glaze.", "price": "2500"}
    ]
    for index, appetizer in enumerate(appetizers, start=1):
        print("{:<5} | {:<20} | {:<90} | {:<10}".format(index, appetizer["name"], appetizer["description"], appetizer["price"]))
    print("-" * 125)
    # Ask user if they want to order appetizers
    print("\nDo you want to order any appetizers? (Enter '1' to order, any other key to go back to the main menu)")
    order_choice = input()
    if order_choice == '1':
        order_appetizers()

# Function to handle ordering appetizers
def order_appetizers():
    print("\nWelcome to the Appetizers Menu!")
    print("Please enter your name:")
    name = input()
    ordered_items = []
    while True:
        print("\nEnter the number in front of the item you wish to order (or enter '6' to go back to the Main Menu):")
        choice = input()
        if choice == '6':
            break
        elif choice.isdigit() and 1 <= int(choice) <= 5:
            ordered_items.append(choice)
        else:
            print("Invalid choice. Please try again.")
    if ordered_items:
        with open("orders.txt", "a") as file:
            for item in ordered_items:
                file.write(f"{name} - {time.strftime('%Y-%m-%d %H:%M:%S')} - Appetizer {item}\n")
        print("Your order has been placed!")
    else:
        print("No items were ordered.")

# Function to display main courses
def display_main_courses():
    print("\nMain Courses:")
    print("{:<5} | {:<20} | {:<90} | {:<10}".format("No.", "Main Course", "Description", "Price (RWF)"))
    print("-" * 125)
    main_courses = [
        {"name": "Spaghetti Carbonara", "description": "Pasta with eggs, cheese, bacon, and black pepper.", "price": "3000"},
        {"name": "Grilled Salmon", "description": "Fresh salmon fillet grilled to perfection.", "price": "4500"},
        {"name": "Chicken Parmesan", "description": "Breaded chicken topped with marinara sauce and cheese, served with spaghetti.", "price": "3800"},
        {"name": "Vegetable Stir-Fry", "description": "Assorted vegetables stir-fried with tofu in a savory sauce, served with rice.", "price": "3200"},
        {"name": "Steak Frites", "description": "Grilled steak served with French fries and salad.", "price": "5000"}
    ]
    for index, main_course in enumerate(main_courses, start=1):
        print("{:<5} | {:<30} | {:<60} | {:<10}".format(index, main_course["name"], main_course["description"], main_course["price"]))
    print("-" * 125)

# Function to display desserts
def display_desserts():
    print("\nDesserts:")
    print("{:<5} | {:<30} | {:<60} | {:<10}".format("No.", "Dessert", "Description", "Price (RWF)"))
    print("-" * 125)
    desserts = [
        {"name": "Tiramisu", "description": "Classic Italian dessert made with layers of coffee-soaked ladyfingers and mascarpone cheese.", "price": "2500"},
        {"name": "Chocolate Lava Cake", "description": "Warm chocolate cake with a gooey chocolate center, served with vanilla ice cream.", "price": "2800"},
        {"name": "New York Cheesecake", "description": "Creamy cheesecake with a graham cracker crust, topped with fresh berries.", "price": "2700"},
        {"name": "Fruit Salad", "description": "Fresh seasonal fruits served with honey and mint.", "price": "2000"},
        {"name": "Creme Brulee", "description": "Rich custard topped with caramelized sugar.", "price": "2600"}
    ]
    for index, dessert in enumerate(desserts, start=1):
        print("{:<5} | {:<30} | {:<60} | {:<10}".format(index, dessert["name"], dessert["description"], dessert["price"]))
    print("-" * 125)

# Function to display beverages
def display_beverages():
    print("\nBeverages:")
    print("{:<5} | {:<30} | {:<60} | {:<10}".format("No.", "Beverage", "Description", "Price (RWF)"))
    print("-" * 125)
    beverages = [
        {"name": "Coke", "description": "Classic Coca-Cola.", "price": "1000"},
        {"name": "Iced Tea", "description": "Refreshing iced tea.", "price": "1200"},
        {"name": "Orange Juice", "description": "Freshly squeezed orange juice.", "price": "1500"},
        {"name": "Cappuccino", "description": "Espresso with steamed milk and froth.", "price": "1800"},
        {"name": "Mineral Water", "description": "Bottled mineral water.", "price": "800"}
    ]
    for index, beverage in enumerate(beverages, start=1):
        print("{:<5} | {:<30} | {:<60} | {:<10}".format(index, beverage["name"], beverage["description"], beverage["price"]))
    print("-" * 125)

# Function to display specials
def display_specials():
    print("\nSpecials:")
    print("{:<5} | {:<30} | {:<60} | {:<10}".format("No.", "Special", "Description", "Price (RWF)"))
    print("-" * 125)
    specials = [
        {"name": "Chef's Special Pasta", "description": "Ask your server for details.", "price": "Varies"},
        {"name": "Seafood Platter", "description": "Assortment of fresh seafood served with dipping sauces.", "price": "Varies"},
        {"name": "Ratatouille", "description": "Classic French stewed vegetable dish.", "price": "Varies"}
    ]
    for index, special in enumerate(specials, start=1):
        print("{:<5} | {:<30} | {:<60} | {:<10}".format(index, special["name"], special["description"], special["price"]))
    print("-" * 125)

# Function to display vegetarian options
def display_vegetarian_options():
    print("\nVegetarian Options:")
    print("{:<5} | {:<30} | {:<60} | {:<10}".format("No.", "Vegetarian Option", "Description", "Price (RWF)"))
    print("-" * 125)
    vegetarian_options = [
        {"name": "Eggplant Parmesan", "description": "Breaded and fried eggplant topped with marinara sauce and cheese, served with spaghetti.", "price": "3200"},
        {"name": "Vegetable Curry", "description": "Assorted vegetables cooked in a spicy curry sauce, served with rice.", "price": "2800"},
        {"name": "Quinoa Salad", "description": "Quinoa mixed with vegetables and herbs, dressed with lemon vinaigrette.", "price": "2500"}
    ]
    for index, option in enumerate(vegetarian_options, start=1):
        print("{:<5} | {:<30} | {:<60} | {:<10}".format(index, option["name"], option["description"], option["price"]))
    print("-" * 125)


# Function to exit the program
def exit_program():
    print("Closing App. Please wait for a few seconds to finish...")
    time.sleep(0.6)
    exit()

# Main menu function
def main_menu():
    display_menu()
    choice = input("\nEnter your choice (1-7): ")

    # Call the function corresponding to the user's choice
    handle_choice(choice)

# Main code execution
if __name__ == "__main__":
    load()
    while True:
        main_menu()
