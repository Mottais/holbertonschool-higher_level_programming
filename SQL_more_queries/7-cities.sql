-- cré une base de données 'hbtn_0d_usa' si elle n'existe pas

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- cré une table 'cities' dans la base de données 'hbtn_0d_usa' si elle n'existe pas
-- avec les colonnes id (INT incrémenté automatiquement et défini comme clé primaire)
-- state_id (INT NON NULL) et name (VARCHAR(256) NON NULL)
-- state_id est une clé étrangère qui référence la colonne id de la table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
