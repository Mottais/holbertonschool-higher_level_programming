-- Crée une table 'id_not_null' dans la base de données actuelle si elle n'existe pas
-- avec les colonnes id (INT avec la valeur par défaut à 1) et name (VARCHAR(256))
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
