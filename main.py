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
    print("****************** Welcome to our App *****************")
    print("*******************************************************\n")
    print("What would you like to do today?\n")
    print("╔═══════════════════════════════════════════════════╗")
    print("║                  Main Menu                        ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║    1. Appetizers                                  ║")
    print("║    2. Main Courses                                ║")
    print("║    3. Desserts                                    ║")
    print("║    4. Beverages                                   ║")
    print("║    5. Specials                                    ║")
    print("║    6. Vegetarian Options                          ║")
    print("║    7. Confirm Order                               ║")
    print("║    8. Exit                                        ║")
    print("╚═══════════════════════════════════════════════════╝")

# Function to handle user's choice
def handle_choice(choice):
    if choice == '1':
        display_category("Appetizers")
    elif choice == '2':
        display_category("Main Courses")
    elif choice == '3':
        display_category("Desserts")
    elif choice == '4':
        display_category("Beverages")
    elif choice == '5':
        display_category("Specials")
    elif choice == '6':
        display_category("Vegetarian Options")
    elif choice == '7':
        confirm_order()
    elif choice == '8':
        exit_program()
    else:
        print("Invalid choice. Please try again.")

# Function to display items of a specific category in tabular format
def display_category(category_name):
    print(f"\n{category_name}:")
    print_table(["No.", "Item", "Description", "Price (RWF)"], [
        {"name": "Item1", "description": "Description1", "price": "1000"},
        {"name": "Item2", "description": "Description2", "price": "1500"},
        {"name": "Item3", "description": "Description3", "price": "2000"},
        {"name": "Item4", "description": "Description4", "price": "1800"},
        {"name": "Item5", "description": "Description5", "price": "2500"}
    ])

# Function to display and handle order confirmation
def confirm_order():
    # Implement confirmation logic here
    print("Order Confirmation Logic")

# Function to exit the program
def exit_program():
    print("Closing App. Please wait for a few seconds to finish...")
    time.sleep(0.6)
    exit()

# Function to print a table with given headers and data
def print_table(headers, data):
    print("{:<5} | {:<25} | {:<70} | {:<10}".format(*headers))
    print("-" * 125)
    for index, item in enumerate(data, start=1):
        print("{:<5} | {:<25} | {:<70} | {:<10}".format(index, item["name"], item["description"], item["price"]))
    print("-" * 125)
    print("{:<5} | {:<25} | {:<70} | {:<10}".format("6", "Go back to Main Menu", "", ""))

# Function to order an item
def order_item(category_name, items):
    print(f"\nWelcome to the {category_name} Menu!")
    print("Please enter your name:")
    name = input()
    ordered_items = []
    while True:
        print("\nEnter the number in front of the item you wish to order (or enter '6' to go back to the Main Menu):")
        choice = input()
        if choice == '6':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(items):
            ordered_items.append(items[int(choice) - 1]["name"])
        else:
            print("Invalid choice. Please try again.")
    if ordered_items:
        with open("orders.txt", "a") as file:
            for item in ordered_items:
                file.write(f"{name} - {time.strftime('%Y-%m-%d %H:%M:%S')} - {category_name} - {item}\n")
        print("Your order has been placed!")
    else:
        print("No items were ordered.")

# Main menu function
def main_menu():
    display_menu()
    choice = input("\nEnter your choice (1-8): ")

    # Call the function corresponding to the user's choice
    handle_choice(choice)

# Main code execution
if __name__ == "__main__":
    load()
    while True:
        main_menu()
