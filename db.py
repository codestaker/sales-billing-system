import sqlite3

# Initialize and create tables
def create_tables():
    conn = sqlite3.connect('sales_system.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT, price REAL)''')
    conn.commit()
    conn.close()

# Add a new user (admin or cashier)
def add_user(username, password, role):
    conn = sqlite3.connect('sales_system.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()

# Get user details (admin or cashier)
def get_user(username, role):
    conn = sqlite3.connect('sales_system.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND role=?", (username, role))
    user = c.fetchone()
    conn.close()
    return user

# Add a new product
def add_product(product_name, price):
    conn = sqlite3.connect('sales_system.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", (product_name, price))
    conn.commit()
    conn.close()

# Get all products
def get_products():
    conn = sqlite3.connect('sales_system.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products
