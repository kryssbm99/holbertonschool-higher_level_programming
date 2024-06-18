-- List California cities (no JOIN, using subquery)
SELECT cities.id, cities.name
FROM `{{ database_name }}`.`cities`
WHERE cities.state_id = (
  SELECT id
  FROM `{{ database_name }}`.`states`
  WHERE name = 'California'
);
ORDER BY cities.id ASC;