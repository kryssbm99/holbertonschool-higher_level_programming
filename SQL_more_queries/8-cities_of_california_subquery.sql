-- Get California state ID (assuming it's unique)
SELECT id FROM `hbtn_0d_usa`.`states` WHERE name = 'California';

-- Set variable to store California state ID (if found)
SET california_state_id = (SELECT id FROM `hbtn_0d_usa`.`states` WHERE name = 'California');

-- List cities in California (if California state ID exists)
SELECT * FROM `hbtn_0d_usa`.`cities` WHERE state_id = california_state_id
ORDER BY id ASC;