-- List genres of Dexter (using a single SELECT)
 SELECT tv_genres.name FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE title = 'Dexter' ORDER BY tv_genres.name;
