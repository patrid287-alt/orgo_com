-- Patel Control Panel - Database Schema
-- Database: storemag

CREATE DATABASE IF NOT EXISTS storemag;
USE storemag;

CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    prodnm VARCHAR(100) NOT NULL,
    qty INT NOT NULL DEFAULT 0,
    mrp DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    payment_mode VARCHAR(50) NOT NULL,
    product_details TEXT,
    total_price DECIMAL(10, 2) NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data (optional)
-- INSERT INTO product (category, prodnm, qty, mrp) VALUES ('Grocery', 'Rice 1kg', 50, 60.00);
