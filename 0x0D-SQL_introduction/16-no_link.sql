-- lists all record without listing rows
-- that don't have name value

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
