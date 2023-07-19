-- list all cities contained in a database
-- Uses SELECT once
-- orders in ascending order using specific

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
