#!/usr/bin/python3
"""Module listing all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    'Sélectionne le texte qui précède le point-virgule (si existe)'
    'dans argv[4] pour éviter les injections SQL.'
    argv_4 = argv[4].split(';')[0]

    curs = connexion.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE '{}%'
                 ORDER BY id;""".format(argv_4))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    connexion.close()
