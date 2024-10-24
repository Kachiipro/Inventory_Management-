--You can change  the database name
--Create database

CREATE DATABASE IF NOT EXISTS Store;

--create table 

CREATE TABLE IF NOT EXISTS My_Inventory(product_id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(50) NOT NULL UNIQUE, product_category VARCHAR(50) NOT NULL, product_quantity INT NOT NULL, product_price INT NOT NULL);