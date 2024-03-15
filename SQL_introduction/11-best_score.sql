-- Liste des noms et scores des joueurs ayant un score supérieur ou égal à 10, triés par score décroissant.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
