-- Lists score and number of records per score (hbtn_0c_0 database).

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
