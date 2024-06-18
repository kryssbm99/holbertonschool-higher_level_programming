-- List all shows with genre names (using a single SELECT)
SELECT t.title, COALESCE(tg.name, NULL) AS genre_name
FROM `{{ database_name }}`.`tv_shows` AS t
LEFT JOIN `{{ database_name }}`.`tv_show_genres` AS tg ON t.id = tg.tv_show_id
ORDER BY t.title ASC, genre_name ASC;
