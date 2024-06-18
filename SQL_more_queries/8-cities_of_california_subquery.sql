-- Select all cities where the state_id matches the California
SELECT * 
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;