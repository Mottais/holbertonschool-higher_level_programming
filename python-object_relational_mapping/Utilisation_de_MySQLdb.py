#!/usr/bin/python3
"""Module listing all states from the database"""
import MySQLdb

connexion = MySQLdb.connect(
    host="localhost",
    port=3306,
    user='root',
    passwd='root',
    )

" Remarque : on peut ajouter db='BD_TEST' dans les parametres de la connexion,"
" cela évite de faire un USE 'BD_TEST' dans la requête SQL, mais pour cela il "
"faut s'assurer que la base de données BD_TEST existe déjà."


# Créer un objet de curseur pour exécuter des requêtes SQL
curseur = connexion.cursor()

curseur.execute("""CREATE DATABASE IF NOT EXISTS BD_TEST""")
curseur.execute("""USE BD_TEST""")
# Créer une table states et une table cities
curseur.execute("""DROP TABLE IF EXISTS cities""")
curseur.execute("""DROP TABLE IF EXISTS states""")
curseur.execute("""CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
                )""")

curseur.execute("""INSERT INTO states (name) VALUES
                ("California"),
                ("Arizona"),
                ("Texas"),
                ("New York"),
                ("Nevada")
                """)

curseur.execute("""CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
                )""")


curseur.execute("""INSERT INTO cities (state_id, name) VALUES
                (1, "San Francisco"),
                (1, "San Jose"),
                (1, "Los Angeles"),
                (1, "Fremont"),
                (1, "Livermore"),
                (2, "Page"),
                (2, "Phoenix"),
                (3, "Dallas"),
                (3, "Houston"),
                (3, "Austin"),
                (4, "New York"),
                (5, "Las Vegas"),
                (5, "Reno"),
                (5, "Henderson"),
                (5, "Carson City")
                """)


# Exécuter une requête pour récupérer les noms des tables dans la base de données actuelle
curseur.execute("SHOW TABLES")

# Récupérer les résultats de la requête
resultats = curseur.fetchall()
print("Tables:")
for row in resultats:
    print(row[0])

# Liste tous les états de la base de données
print("Tous les états de la base de données :")
curseur.execute("""SELECT * FROM states ORDER BY id""")
rows = curseur.fetchall()
print(rows)
for row in rows:
    print(row)

# Liste toutes les villes de la base de données
print("Toutes les villes de la base de données :")
curseur.execute("""SELECT * FROM cities ORDER BY id""")
rows = curseur.fetchall()
print(rows)
for row in rows:
    print(row)

# Liste tous les états dont le nom commence par N (N majuscule)
Lettre = 'N'
print("Tous les états de la base de données qui commence par 'N':")
curseur.execute("""SELECT * FROM states
                WHERE BINARY name LIKE '{}%' ORDER BY id;""".format(Lettre))
rows = curseur.fetchall()
for row in rows:
    print(row)

# Liste les villes et leur état : jointure de 2 tables"""
print("Liste des villes et leur état :")
curseur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """)
rows = curseur.fetchall()
for row in rows:
    print(row)

# NE PAS OUBLIER D'ENREGISTRER LES MODIFICATIONS DANS LA BASE DE DONNÉES
# Enregistrer les modifications dans la base de données
connexion.commit()


# Fermer le curseur
curseur.close()


# Fermer la connexion
connexion.close()
