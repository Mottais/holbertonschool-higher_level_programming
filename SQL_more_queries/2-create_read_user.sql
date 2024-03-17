-- Crée une base de données hbtn_0d_2 si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Crée l'utilisateur user_0d_2 s'il n'existe pas avec mot de passe 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Accorde à l'utilisateur user_0d_2 le droit de lire la base de données hbtn_0d_2 (dans localhost)
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
