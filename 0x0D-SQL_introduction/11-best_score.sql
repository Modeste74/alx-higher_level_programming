-- lists all record with a score
-- equal to or above 10

SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
