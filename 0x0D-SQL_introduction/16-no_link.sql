-- lists all record without listing rows
-- that don't have name value

SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL
ORDERED BY score DESC;