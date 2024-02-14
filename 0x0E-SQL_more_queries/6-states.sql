-- creates a database, atable in that database and a primary key in the table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- switches to the database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS state(id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(256) NOT NULL);
