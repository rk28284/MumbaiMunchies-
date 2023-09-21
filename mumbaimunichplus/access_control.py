class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, password, role):
        hashed_password = self.hash_password(password)
        user = User(username, hashed_password, role)
        self.users.append(user)

    def authenticate_user(self, username, password):
        user = self.find_user_by_username(username)
        if user and self.check_password(password, user.password):
            return True
        return False

    def find_user_by_username(self, username):
        return next((user for user in self.users if user.username == username), None)

    def hash_password(self, password):
        # Implement password hashing here (e.g., using bcrypt)
        pass

    def check_password(self, input_password, hashed_password):
        # Implement password checking here (e.g., using bcrypt)
        pass

# Sample usage:
user_manager = UserManager()

# Add users with roles and hashed passwords
user_manager.add_user("admin", "admin123", "admin")
user_manager.add_user("staff", "staff123", "canteen_staff")
user_manager.add_user("cashier", "cashier123", "cashier")

# Authenticate a user
authenticated = user_manager.authenticate_user("admin", "admin123")
if authenticated:
    user_role = user_manager.find_user_by_username("admin").role
    print(f"Authenticated as {user_role} user.")
else:
    print("Authentication failed.")
