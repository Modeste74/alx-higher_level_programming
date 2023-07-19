-- lists a field contected to state field found in a certain database
-- order by a certain field in a certain order

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC;
