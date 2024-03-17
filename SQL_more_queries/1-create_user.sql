-- Création de l'utilisateur user_0d_1 s'il n'existe pas avec mot de passe 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Accorde tous les privilèges à l'utilisateur user_0d_1 sur toutes les bases de données
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
