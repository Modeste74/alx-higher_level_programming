-- displays the top 3 cities temps during
-- the specific month periods

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
ORDER BY temperatures DESC
LIMIT 3;
