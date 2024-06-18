-- List shows with linked genres (using a single SELECT)
SELECT t.title, tg.genre_id
FROM `{{ database_name }}`.`tv_shows` AS t
INNER JOIN `{{ database_name }}`.`tv_show_genres` AS tg ON t.id = tg.tv_show_id
GROUP BY t.id
HAVING COUNT(tg.genre_id) > 0
ORDER BY t.title ASC, tg.genre_id ASC;