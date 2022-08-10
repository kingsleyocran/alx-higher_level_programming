-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
-- states description: id INT unique, auto generated, can’t be null and is a primary key and name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));