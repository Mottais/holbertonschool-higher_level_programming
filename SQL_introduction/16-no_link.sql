-- Liste la table qui a des nom valides (non vides ou non nuls) et les scores dans l'ordre décroissant
-- SELECT id, score, name FROM second_table WHERE (name != '' AND name IS NOT NULL) ORDER BY score DESC;

-- Liste la table qui a des noms (non nuls) et les scores dans l'ordre décroissant
SELECT id, score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
