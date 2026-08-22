import tkinter as tk
from tkinter import messagebox
import mysql.connector
from docx import Document


# MySQL Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="storemag"
    )


# Function to fetch products from the database
def get_products_by_category(category=""):
    connection = get_db_connection()
    cursor = connection.cursor()

    if category:
        query = "SELECT * FROM product WHERE category LIKE %s"
        cursor.execute(query, ('%' + category + '%',))
    else:
        query = "SELECT * FROM product"
        cursor.execute(query)
        # Store Panel to show products category-wise
def show_store_panel():
    clear_screen()

    label_info = tk.Label(
        window,
        text="Store Management",
        font=("Arial", 12)
    )
    label_info.pack(pady=20)

    label_category = tk.Label(
        window,
        text="Enter Category (optional):"
    )
    label_category.pack(pady=5)

    entry_category = tk.Entry(window)
    entry_category.pack(pady=5)

    button_search = tk.Button(
        window,
        text="Search",
        command=lambda: display_products(entry_category.get())
    )
    button_search.pack(pady=5)


# Display products
def display_products(category):
    clear_screen()

    label_category = tk.Label(
        window,
        text="Store Management",
        font=("Arial", 12)
    )
    label_category.pack(pady=20)

    products = get_products_by_category(category)

    cart_items = {}

    def update_cart_display():
        cart_display.delete(0, tk.END)

        for name, qty in cart_items.items():
            cart_display.insert(
                tk.END,
                f"{name} - Qty: {qty}"
            )

    def add_to_cart(product_id, name, price, available_qty):
        if name in cart_items:
            if cart_items[name] < available_qty:
                cart_items[name] += 1
            else:
                messagebox.showwarning(
                    "Stock Limit",
                    f"Cannot add more than available quantity "
                    f"({available_qty}) for {name}."
                )
        else:
            if available_qty > 0:
                cart_items[name] = 1
            else:
                messagebox.showwarning(
                    "Out of Stock",
                    f"{name} is out of stock."
                )

        update_cart_display()

    def remove_from_cart(product_id, name):
        if name in cart_items and cart_items[name] > 0:
            cart_items[name] -= 1

            if cart_items[name] == 0:
                del cart_items[name]

        update_cart_display()

    # Display products with + and - buttons
    for product in products:
        product_id, category, name, qty, mrp = product

        product_frame = tk.Frame(window)
        product_frame.pack(
            fill=tk.X,
            padx=10,
            pady=5
        )

        product_label = tk.Label(
            product_frame,
            text=f"{name} - ${mrp} (Available: {qty})",
            width=50,
            anchor="w"
        )
        product_label.pack(
            side=tk.LEFT,
            padx=5
        )

        button_add = tk.Button(
            product_frame,
            text="+",
            command=lambda pid=product_id,
                           pname=name,
                           pprice=mrp,
                           pqty=qty:
            add_to_cart(pid, pname, pprice, pqty)
        )
        button_add.pack(
            side=tk.LEFT,
            padx=5
        )

        button_remove = tk.Button(
            product_frame,
            text="-",
            command=lambda pid=product_id,
                           pname=name:
            remove_from_cart(pid, pname)
        )
        button_remove.pack(
            side=tk.LEFT,
            padx=5
        )

    cart_display = tk.Listbox(
        window,
        width=50,
        height=10
    )
    cart_display.pack(pady=20)

    button_proceed_to_bill = tk.Button(
        window,
        text="Proceed to Bill",
        command=lambda: show_bill_panel(cart_items)
    )
    button_proceed_to_bill.pack(pady=10)

    products = cursor.fetchall()
    connection.close()

    return products
    # Store Panel to show products category-wise
def show_store_panel():
    clear_screen()

    label_info = tk.Label(
        window,
        text="Store Management",
        font=("Arial", 12)
    )
    label_info.pack(pady=20)

    label_category = tk.Label(
        window,
        text="Enter Category (optional):"
    )
    label_category.pack(pady=5)

    entry_category = tk.Entry(window)
    entry_category.pack(pady=5)

    button_search = tk.Button(
        window,
        text="Search",
        command=lambda: display_products(entry_category.get())
    )
    button_search.pack(pady=5)


# Display products
def display_products(category):
    clear_screen()

    label_category = tk.Label(
        window,
        text="Store Management",
        font=("Arial", 12)
    )
    label_category.pack(pady=20)

    products = get_products_by_category(category)

    cart_items = {}

    def update_cart_display():
        cart_display.delete(0, tk.END)

        for name, qty in cart_items.items():
            cart_display.insert(
                tk.END,
                f"{name} - Qty: {qty}"
            )

    def add_to_cart(product_id, name, price, available_qty):
        if name in cart_items:
            if cart_items[name] < available_qty:
                cart_items[name] += 1
            else:
                messagebox.showwarning(
                    "Stock Limit",
                    f"Cannot add more than available quantity "
                    f"({available_qty}) for {name}."
                )
        else:
            if available_qty > 0:
                cart_items[name] = 1
            else:
                messagebox.showwarning(
                    "Out of Stock",
                    f"{name} is out of stock."
                )

        update_cart_display()

    def remove_from_cart(product_id, name):
        if name in cart_items and cart_items[name] > 0:
            cart_items[name] -= 1

            if cart_items[name] == 0:
                del cart_items[name]

        update_cart_display()

    # Display products with + and - buttons
    for product in products:
        product_id, category, name, qty, mrp = product

        product_frame = tk.Frame(window)
        product_frame.pack(
            fill=tk.X,
            padx=10,
            pady=5
        )

        product_label = tk.Label(
            product_frame,
            text=f"{name} - ${mrp} (Available: {qty})",
            width=50,
            anchor="w"
        )
        product_label.pack(
            side=tk.LEFT,
            padx=5
        )

        button_add = tk.Button(
            product_frame,
            text="+",
            command=lambda pid=product_id,
                           pname=name,
                           pprice=mrp,
                           pqty=qty:
            add_to_cart(pid, pname, pprice, pqty)
        )
        button_add.pack(
            side=tk.LEFT,
            padx=5
        )

        button_remove = tk.Button(
            product_frame,
            text="-",
            command=lambda pid=product_id,
                           pname=name:
            remove_from_cart(pid, pname)
        )
        button_remove.pack(
            side=tk.LEFT,
            padx=5
        )

    cart_display = tk.Listbox(
        window,
        width=50,
        height=10
    )
    cart_display.pack(pady=20)

    button_proceed_to_bill = tk.Button(
        window,
        text="Proceed to Bill",
        command=lambda: show_bill_panel(cart_items)
    )
    button_proceed_to_bill.pack(pady=10)
