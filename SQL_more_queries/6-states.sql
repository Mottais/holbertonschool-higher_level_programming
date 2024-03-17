-- Crée une base de données hbtn_0d_usa si elle n'existe pas dans le serveur MySQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Crée une table 'states' dans la base de données hbtn_0d_usa si elle n'existe pas
-- avec les colonnes id (INT incrémenté automaiquement et défini comme clé primaire) et name (VARCHAR(256) NON NULL)
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
