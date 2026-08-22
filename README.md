# Patel Control Panel

A smart and interactive Store Management System that brings inventory, shopping, and automated billing together in one Python-based platform.

## 🚀 Features

- Product management
- Inventory management
- Shopping cart management
- Customer billing
- Automatic bill generation
- MySQL database integration
- Interactive graphical user interface
- Admin and store management

## 🛠️ Technologies Used

- Python
- Tkinter
- MySQL
- MySQL Connector
- Python-docx

## 📌 Project Overview

Patel Control Panel is a Store Management System developed to make everyday store operations easier and more organized.

The system provides a graphical interface through which products can be managed, inventory can be maintained, products can be added to a shopping cart, and customer bills can be generated.

The project combines Python for application logic, Tkinter for the graphical interface, MySQL for database management, and Python-docx for generating bills.

## 🎯 Objectives

- To simplify store and product management.
- To maintain product and inventory information.
- To provide an easy-to-use shopping interface.
- To manage selected products through a shopping cart.
- To calculate the total bill efficiently.
- To generate customer bills automatically.
- To store and manage product information using MySQL.

## 📂 Main Modules

### 👨‍💼 Admin

The Admin module is used for managing store-related information and products.

### 🛒 Store

The Store module allows users to view available products and manage their shopping cart.

### 🧾 Billing

The Billing module handles customer billing and generates the final bill based on the selected products.

### 🗄️ Database

MySQL is used to store and manage product and store information.

## 🔄 System Flow

```text
Admin
  ↓
Product Management
  ↓
Store
  ↓
Select Products
  ↓
Shopping Cart
  ↓
Calculate Bill
  ↓
Generate Bill

```text
patel-control-panel/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── admin.py
│   ├── store.py
│   ├── billing.py
│   ├── database.py
│   └── config.py
│
├── database/
│   └── database.sql
│
├── bills/
│
├── assets/
│
└── docs/
