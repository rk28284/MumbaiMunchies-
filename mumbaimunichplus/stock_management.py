class Snack:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class StockManager:
    def __init__(self):
        self.stock = []

    def add_snack(self, name, category, price, quantity):
        snack = Snack(name, category, price, quantity)
        self.stock.append(snack)

    def update_snack_quantity(self, name, quantity_change):
        snack = self.find_snack_by_name(name)
        if snack:
            snack.quantity += quantity_change
        else:
            raise Exception(f"Snack '{name}' not found in stock.")

    def remove_snack(self, name):
        snack = self.find_snack_by_name(name)
        if snack:
            self.stock.remove(snack)
        else:
            raise Exception(f"Snack '{name}' not found in stock.")

    def get_snack_by_category(self, category):
        return [snack for snack in self.stock if snack.category == category]

    def find_snack_by_name(self, name):
        return next((snack for snack in self.stock if snack.name == name), None)

# Sample usage:
stock_manager = StockManager()

# Add snacks to the stock
stock_manager.add_snack("Chips", "Snacks", 2.5, 50)
stock_manager.add_snack("Coke", "Beverages", 1.5, 100)
stock_manager.add_snack("Brownie", "Desserts", 3.0, 30)

# Update snack quantity
try:
    stock_manager.update_snack_quantity("Chips", 10)
except Exception as e:
    print(f"Error: {str(e)}")

# Remove a snack
try:
    stock_manager.remove_snack("Coke")
except Exception as e:
    print(f"Error: {str(e)}")

# Get snacks in a specific category
snacks_in_category = stock_manager.get_snack_by_category("Snacks")
for snack in snacks_in_category:
    print(f"{snack.name} - {snack.price} - Quantity: {snack.quantity}")
