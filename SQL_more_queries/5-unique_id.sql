-- cré une table 'unique_id' dans la base de données actuelle si elle n'existe pas
-- avec les colonnes id (INT avec une valeur unique par défaut à 1) et name (VARCHAR(256))
-- Une requête d'insertion dans cette table doit échouer si l'id existe déjà
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
