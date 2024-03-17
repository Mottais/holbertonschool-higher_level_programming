-- liste toutes les émissions contenues dans hbtn_0d_tvshows qui ont au moins un genre lié
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
