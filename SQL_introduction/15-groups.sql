-- Liste et compte le nombre de scores dans la table second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
