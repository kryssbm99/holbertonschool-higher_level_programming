-- List genres of Dexter (using a single SELECT)
SELECT g.name
FROM `{{ database_name }}`.`genres` AS g
INNER JOIN `{{ database_name }}`.`tv_show_genres` AS tg ON g.id = tg.genre_id
INNER JOIN `{{ database_name }}`.`tv_shows` AS t ON tg.tv_show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY g.name ASC;
