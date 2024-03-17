-- cré une table 'force_name' dans la base de données actuelle si elle n'existe pas
-- avec les colonnes id (INT) et name (VARCHAR(256) NON NULL)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
