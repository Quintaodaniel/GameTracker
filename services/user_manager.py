import csv
import os

class UserManager:
    USERS_FILE = 'users/users.csv'
    HEADERS = ['username', 'password']

    @classmethod
    def ensure_file_exists(cls):
        """Create the CSV file with headers if it doesn't exist."""
        if not os.path.exists(cls.USERS_FILE):
            os.makedirs(os.path.dirname(cls.USERS_FILE), exist_ok=True)
            with open(cls.USERS_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(cls.HEADERS)

    @classmethod
    def user_exists(cls, username):
        """Check if a username already exists."""
        cls.ensure_file_exists()
        with open(cls.USERS_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return any(row['username'] == username for row in reader)

    @classmethod
    def create_user(cls, username, password):
        """Create a new user if it doesn't already exist."""
        cls.ensure_file_exists()
        if cls.user_exists(username):
            return False  # user already exists
        with open(cls.USERS_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
        return True

    @classmethod
    def authenticate(cls, username, password):
        """Check if username and password match."""
        cls.ensure_file_exists()
        with open(cls.USERS_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    return True
        return False
