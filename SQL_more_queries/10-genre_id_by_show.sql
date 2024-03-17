-- liste toutes les émissions contenues dans hbtn_0d_tvshows qui ont au moins un genre lié
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON show_id = tv_shows.id
WHERE genre_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

-- Autre solution :
-- SELECT title, genre_id
-- FROM tv_show_genres
-- LEFT JOIN tv_shows ON show_id=tv_shows.id
-- ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
