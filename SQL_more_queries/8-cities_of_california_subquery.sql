-- Sous requête pour obtenir les villes de Californie
SET @california_id := (SELECT id FROM states WHERE name = 'California');
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;

-- autre méthode
-- SELECT id, name
-- FROM cities
-- WHERE state_id = (SELECT id FROM states WHERE name="California")
-- ORDER BY id ASC;

