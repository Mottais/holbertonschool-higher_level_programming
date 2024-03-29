#!/usr/bin/python3
"""Liste tous les états dont le nom commence par N (N majuscule)"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    curs = connexion.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE 'N%' ORDER BY id;""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    connexion.close()
