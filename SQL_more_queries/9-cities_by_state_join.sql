-- List all cities with state names (using a single SELECT)
SELECT c.id, c.name, s.name AS state_name
FROM `{{ database_name }}`.`cities` AS c
INNER JOIN `{{ database_name }}`.`states` AS s ON c.state_id = s.id
ORDER BY c.id ASC;