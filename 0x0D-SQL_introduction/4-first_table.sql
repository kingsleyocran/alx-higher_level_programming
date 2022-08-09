-- creates a table called first_table in the current database in your MySQL server
-- ignores if it already exists (so that code doesnt fail)
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));