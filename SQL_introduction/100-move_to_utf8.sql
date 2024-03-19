-- Convertir la base de données en UTF8 (utf8mb4) avec la collation utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

-- Convertir la table en UTF8 (utf8mb4) avec la collation utf8mb4_unicode_ci
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Convertir le champ spécifique en UTF8 (utf8mb4) avec la collation utf8mb4_unicode_ci
ALTER TABLE first_table
    MODIFY field_name VARCHAR(255)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
