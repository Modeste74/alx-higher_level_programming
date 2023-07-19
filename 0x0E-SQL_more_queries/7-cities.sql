-- creates a database and a table
-- the field in the table have specific requirements
-- uniqueness, auto-generated, primary key, foreign key, can't null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id),
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	);
