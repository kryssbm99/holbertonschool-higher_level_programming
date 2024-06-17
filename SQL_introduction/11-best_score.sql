-- Lists score and name (ordered by score) with score >= 10 from second_table in hbtn_0c_0 database.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
