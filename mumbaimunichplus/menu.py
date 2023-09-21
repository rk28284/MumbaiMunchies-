import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the main menu
def main_menu(user_manager, stock_manager, sales_analytics, canteen_manager):
    clear_screen()
    print("Welcome to Mumbai Munchies - Canteen Management System")
    print("-----------------------------------------")
    print("1. View Menu")
    print("2. Place Order")
    print("3. Check Out")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu(stock_manager)
    elif choice == "2":
        username = input("Enter your username: ")
        if user_manager.authenticate_user(username):
            place_order(username, stock_manager, canteen_manager)
        else:
            print("Authentication failed. Please enter valid credentials.")
    elif choice == "3":
        # Implement checkout functionality here
        pass
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")

# Function to display the menu
def display_menu(stock_manager):
    clear_screen()
    print("Menu")
    print("-----------------------------------------")
    
    # Get snacks in different categories and display them
    categories = ["Snacks", "Beverages", "Desserts"]
    for category in categories:
        snacks_in_category = stock_manager.get_snack_by_category(category)
        print(f"{category}:")
        for snack in snacks_in_category:
            print(f"{snack.name} - ${snack.price} - Quantity: {snack.quantity}")
    
    print("4. Back to Main Menu")

# Function to place an order
def place_order(username, stock_manager, canteen_manager):
    clear_screen()
    print(f"Place Order for {username}")
    print("-----------------------------------------")
    
    # Display the menu
    display_menu(stock_manager)
    
    item_name = input("Enter the item name you want to order: ")
    quantity = int(input("Enter the quantity: "))
    
    try:
        canteen_manager.place_order(username, item_name, quantity, stock_manager)
        print(f"Order placed successfully: {item_name} x{quantity}")
    except Exception as e:
        print(f"Order failed: {str(e)}")
    
    input("Press Enter to continue...")

# Add any additional functions related to the menu here

