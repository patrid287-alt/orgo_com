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

    products = cursor.fetchall()
    connection.close()

    return products
