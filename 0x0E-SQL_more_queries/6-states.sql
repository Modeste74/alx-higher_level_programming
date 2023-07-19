-- creates a database and a table
-- in the table there should be a field that is unique 
-- should be auto-generated and is a primary key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id),
	name VARCHAR(256) NOT NULL
	);
