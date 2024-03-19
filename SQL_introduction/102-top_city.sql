-- liste les 3 premières villes qui ont la moyenne des température la plus élevée pendant les mois de juillet et août.
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
