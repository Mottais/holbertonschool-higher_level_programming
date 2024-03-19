#!/usr/bin/python3
"""Liste les états
   dont le nom correspond à l'argument passé : argv[4]
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    curs = connexion.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE '{}%'
                 ORDER BY id;""".format(argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    connexion.close()
