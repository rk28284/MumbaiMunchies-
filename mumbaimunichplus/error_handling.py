class CanteenError(Exception):
    pass

class UserNotFoundError(CanteenError):
    def __init__(self, username):
        self.username = username

class InsufficientStockError(CanteenError):
    def __init__(self, item_name, required_quantity, available_quantity):
        self.item_name = item_name
        self.required_quantity = required_quantity
        self.available_quantity = available_quantity

class InvalidChoiceError(CanteenError):
    def __init__(self, choice):
        self.choice = choice

class CanteenManager:
    def __init__(self):
        self.users = []
        self.stock = []

    def place_order(self, username, item_name, quantity, stock_manager):
        # Check if the user exists
        user = next((u for u in self.users if u.username == username), None)
        if user is None:
            raise UserNotFoundError(username)

        # Check if the item is in stock and has sufficient quantity
        item = stock_manager.find_snack_by_name(item_name)
        if item is None or item.quantity < quantity:
            raise InsufficientStockError(item_name, quantity, item.quantity)

        # Add logic to process the order
        print(f"Order placed by {username}: {item_name} x{quantity}")

# Sample usage:
canteen_manager = CanteenManager()

# Function to place an order
def place_order(username, item_name, quantity, stock_manager, canteen_manager):
    try:
        canteen_manager.place_order(username, item_name, quantity, stock_manager)
    except UserNotFoundError as e:
        raise UserNotFoundError(e.username)
    except InsufficientStockError as e:
        raise InsufficientStockError(e.item_name, e.required_quantity, e.available_quantity)

# Test placing an order
try:
    place_order("admin", "Chips", 10, stock_manager, canteen_manager)
    place_order("user123", "Coke", 5, stock_manager, canteen_manager)
    place_order("staff", "Brownie", 3, stock_manager, canteen_manager)
    place_order("admin", "Ice Cream", 2, stock_manager, canteen_manager)
except CanteenError as e:
    print(f"Error: {str(e)}")
