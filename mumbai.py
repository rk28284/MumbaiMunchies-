# Define the snack inventory as a dictionary with snack ID as keys and snack details as values.
snack_inventory = {
    1: {"name": "Chips", "price": 10, "available": True},
    2: {"name": "Soda", "price": 20, "available": True},
    3: {"name": "Candy", "price": 5, "available": True},
    4: {"name": "Cookies", "price": 15, "available": True},
    5: {"name": "Burger", "price": 50, "available": True},
    6: {"name": "Pizza", "price": 80, "available": True},
    7: {"name": "Ice Cream", "price": 25, "available": True},
    8: {"name": "Donut", "price": 12, "available": True},
    9: {"name": "French Fries", "price": 30, "available": True},
    10: {"name": "Popcorn", "price": 18, "available": True},
    11: {"name": "Nachos", "price": 22, "available": True},
    12: {"name": "Pretzels", "price": 14, "available": True},
}

# Initialize an empty sales record list.
sales_record = []

# Function to display the snack inventory.
def display_inventory():
    print("\nSnack Inventory:")
    print("ID | Name       | Price | Available")
    print("----------------------------------")
    for snack_id, details in snack_inventory.items():
        print(f"{snack_id}  | {details['name']:<10} | {details['price']:<6} | {'Yes' if details['available'] else 'No'}")

# Function to add a new snack to the inventory.
def add_snack():
    snack_id = len(snack_inventory) + 1
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    available = True  # New snacks are initially available
    snack_inventory[snack_id] = {"name": name, "price": price, "available": available}
    print(f"{name} has been added to the inventory with ID {snack_id}")

# Function to remove a snack from the inventory.
def remove_snack():
    display_inventory()
    snack_id = int(input("Enter the ID of the snack to remove: "))
    if snack_id in snack_inventory:
        snack_name = snack_inventory.pop(snack_id)['name']
        print(f"{snack_name} has been removed from the inventory.")
    else:
        print("Invalid snack ID.")

# Function to update the availability of a snack.
def update_availability():
    display_inventory()
    snack_id = int(input("Enter the ID of the snack to update availability: "))
    if snack_id in snack_inventory:
        new_availability = input("Is the snack available (yes/no)? ").lower()
        if new_availability == "yes":
            snack_inventory[snack_id]["available"] = True
        elif new_availability == "no":
            snack_inventory[snack_id]["available"] = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Invalid snack ID.")

# Function to record a snack sale.
def record_sale():
    display_inventory()
    snack_id = int(input("Enter the ID of the snack sold: "))
    if snack_id in snack_inventory:
        if snack_inventory[snack_id]["available"]:
            sales_record.append({"id": snack_id, "name": snack_inventory[snack_id]["name"], "price": snack_inventory[snack_id]["price"]})
            print(f"{snack_inventory[snack_id]['name']} has been sold.")
            snack_inventory[snack_id]["available"] = False
        else:
            print("This snack is currently unavailable.")
    else:
        print("Invalid snack ID.")

# Main program loop
while True:
    print("\nMumbai Munchies: The Canteen Chronicle")
    print("1. Display Inventory")
    print("2. Add Snack to Inventory")
    print("3. Remove Snack from Inventory")
    print("4. Update Snack Availability")
    print("5. Record Sale")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == "1":
        display_inventory()
    elif choice == "2":
        add_snack()
    elif choice == "3":
        remove_snack()
    elif choice == "4":
        update_availability()
    elif choice == "5":
        record_sale()
    elif choice == "6":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
