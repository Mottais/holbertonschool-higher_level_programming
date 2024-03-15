-- Créé une table second_table avec trois colonnes id (entier), name (256 caracteres) et score (entier) dans la base de données active.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT );

-- puis ajoute 4 lignes dans cette table.
INSERT INTO second_table VALUES (1, 'John', 10);
INSERT INTO second_table VALUES (2, 'Alex', 3);
INSERT INTO second_table VALUES (3, 'Bob', 14);
INSERT INTO second_table VALUES (4, 'George', 8);
