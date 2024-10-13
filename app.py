import streamlit as st
from auth import admin_login, admin_signup, login_user
from db import create_tables, add_product, get_products

# Initialize Database
create_tables()

st.title("Sales Billing System")

# Navigation
menu = ["Home", "Admin Login", "Admin Signup", "Login as Cashier"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Sales Billing System")
    st.write("Use the sidebar to navigate.")
    
elif choice == "Admin Login":
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if admin_login(username, password):
            st.success(f"Welcome, {username}!")
            # Show admin options
            option = st.selectbox("Admin Options", ["Add Product", "View Products"])
            
            if option == "Add Product":
                product_name = st.text_input("Product Name")
                price = st.number_input("Price", min_value=0.0)
                
                if st.button("Add Product"):
                    add_product(product_name, price)
                    st.success(f"Product '{product_name}' added!")
            
            elif option == "View Products":
                st.subheader("Products List")
                products = get_products()
                for product in products:
                    st.write(f"Product: {product[1]}, Price: {product[2]}")
        else:
            st.error("Invalid username or password.")

elif choice == "Admin Signup":
    st.subheader("Admin Signup")
    new_username = st.text_input("Create Admin Username")
    new_password = st.text_input("Create Admin Password", type='password')
    
    if st.button("Signup"):
        if admin_signup(new_username, new_password):
            st.success("Admin account created!")
        else:
            st.error("Admin account already exists or error in signup.")
            
elif choice == "Login as Cashier":
    st.subheader("Cashier Login")
    cashier_username = st.text_input("Cashier Username")
    cashier_password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if login_user(cashier_username, cashier_password):
            st.success(f"Welcome, {cashier_username}!")
            # Cashier can only view products
            st.subheader("Available Products")
            products = get_products()
            for product in products:
                st.write(f"Product: {product[1]}, Price: {product[2]}")
        else:
            st.error("Invalid cashier credentials.")
