-- List California cities (no JOIN, using subquery)
SELECT c.id, c.name
FROM `{{ database_name }}`.`cities` AS c
WHERE c.state_id = (
  SELECT id
  FROM `{{ database_name }}`.`states`
  WHERE name = 'California'
);
ORDER BY c.id ASC;