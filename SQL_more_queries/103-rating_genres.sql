-- Listes les shows avec la somme des notes
SELECT name, SUM(rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres ON id = genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
