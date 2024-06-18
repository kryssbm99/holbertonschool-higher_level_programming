-- List genres with show counts (using a single SELECT)
SELECT g.name AS genre, COUNT(tg.tv_show_id) AS number_of_shows
FROM `{{ database_name }}`.`genres` AS g
LEFT JOIN `{{ database_name }}`.`tv_show_genres` AS tg ON g.id = tg.genre_id
GROUP BY g.id
HAVING COUNT(tg.tv_show_id) > 0
ORDER BY number_of_shows DESC;