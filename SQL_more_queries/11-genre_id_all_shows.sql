-- List all shows with genre IDs (using a single SELECT)
SELECT t.title, COALESCE(tg.genre_id, NULL) AS genre_id
FROM `{{ database_name }}`.`tv_shows` AS t
LEFT JOIN `{{ database_name }}`.`tv_show_genres` AS tg ON t.id = tg.tv_show_id
ORDER BY t.title ASC, genre_id ASC;