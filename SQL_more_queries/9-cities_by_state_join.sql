-- Jointure de deux tables pour afficher les villes avec leur état
-- suivant la condition cities.state_id = states.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
