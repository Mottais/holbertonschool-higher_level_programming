-- liste tous les spectacles sans le genre Comédie
SELECT title FROM tv_shows
WHERE title NOT IN (SELECT title FROM tv_shows
					INNER JOIN tv_show_genres ON tv_shows.id = show_id
					INNER JOIN tv_genres ON tv_genres.id = genre_id
					WHERE name = "Comedy ")
ORDER BY title ASC;
