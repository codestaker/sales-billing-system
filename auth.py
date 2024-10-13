import bcrypt
from db import add_user, get_user

# Admin Login Function
def admin_login(username, password):
    user = get_user(username, "admin")
    if user and bcrypt.checkpw(password.encode(), user[2].encode()):
        return True
    return False

# Admin Signup Function
def admin_signup(username, password):
    user = get_user(username, "admin")
    if user:
        return False  # Admin already exists
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    add_user(username, hashed_password, "admin")
    return True

# Cashier Login Function
def login_user(username, password):
    user = get_user(username, "cashier")
    if user and bcrypt.checkpw(password.encode(), user[2].encode()):
        return True
    return False
