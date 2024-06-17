-- Lists score and name (ordered by score DESC) for valid rows in second_table (hbtn_0c_0 database).

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
