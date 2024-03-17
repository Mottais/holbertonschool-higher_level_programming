--  liste tous les genres de hbtn_0d_tvshows et affiche le nombre d'émissions liées à chacun d'entre eux.
SELECT name AS genre, count(show_id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON genre_id = id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
