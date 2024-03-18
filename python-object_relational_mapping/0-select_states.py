#!/usr/bin/python3
"""Module listing all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    curseur = connexion.cursor()
    curseur.execute("""SELECT * FROM states ORDER BY id""")
    rows = curseur.fetchall()
    for row in rows:
        print(row)
    curseur.close()
    connexion.close()
