-- creates a table with a field that is unique and has a default value

CREATE TABLE IF NOT EXISTS unique_id(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
	);
