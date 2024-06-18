-- List shows without linked genres (using a single SELECT)
SELECT t.title, NULL AS genre_id
FROM `{{ database_name }}`.`tv_shows` AS t
LEFT JOIN `{{ database_name }}`.`tv_show_genres` AS tg ON t.id = tg.tv_show_id
WHERE tg.genre_id IS NULL
ORDER BY t.title ASC;
