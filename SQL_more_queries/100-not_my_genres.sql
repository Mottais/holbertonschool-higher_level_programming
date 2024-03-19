-- Liste les genres de séries qui ne sont pas associés à la série "Dexter"

-- Liste temporaire des genres de la série "Dexter"
DROP TEMPORARY TABLE IF EXISTS Genres_de_Dexter;
CREATE TEMPORARY TABLE Genres_de_Dexter AS
SELECT name FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = show_id
INNER JOIN tv_genres ON tv_genres.id = genre_id
WHERE title = "Dexter"
ORDER by title ASC;

-- Liste des genres de séries qui ne sont pas dans la liste temporaire
SELECT name FROM tv_genres
WHERE name NOT IN (SELECT name FROM Genres_de_Dexter ORDER BY name ASC);
