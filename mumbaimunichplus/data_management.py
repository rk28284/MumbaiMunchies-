import bcrypt
import sqlite3  # You can choose another database library if preferred

class User:
    def __init__(self, username, hashed_password, role):
        self.username = username
        self.hashed_password = hashed_password
        self.role = role

class UserManager:
    def __init__(self):
        # Initialize a SQLite database (you can change the database choice)
        self.conn = sqlite3.connect('canteen.db')
        self.cursor = self.conn.cursor()

        # Create a table for users if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                hashed_password TEXT,
                role TEXT
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password, role):
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.cursor.execute('INSERT INTO users (username, hashed_password, role) VALUES (?, ?, ?)',
                            (username, hashed_password, role))
        self.conn.commit()

    def authenticate_user(self, username, password):
        self.cursor.execute('SELECT hashed_password FROM users WHERE username = ?', (username,))
        row = self.cursor.fetchone()
        if row:
            hashed_password = row[0]
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        return False

    def find_user_by_username(self, username):
        self.cursor.execute('SELECT username, role FROM users WHERE username = ?', (username,))
        row = self.cursor.fetchone()
        if row:
            return User(row[0], None, row[1])
        return None

    def close_connection(self):
        self.conn.close()

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

# Close the database connection when done
user_manager.close_connection()
