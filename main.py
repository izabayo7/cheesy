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

# Function to display appetizers
def display_appetizers():
    print("\nAppetizers:")
    # Display appetizers here

# Function to display main courses
def display_main_courses():
    print("\nMain Courses:")
    # Display main courses here

# Function to display desserts
def display_desserts():
    print("\nDesserts:")
    # Display desserts here

# Function to display beverages
def display_beverages():
    print("\nBeverages:")
    # Display beverages here

# Function to display specials
def display_specials():
    print("\nSpecials:")
    # Display specials here

# Function to display vegetarian options
def display_vegetarian_options():
    print("\nVegetarian Options:")
    # Display vegetarian options here

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
