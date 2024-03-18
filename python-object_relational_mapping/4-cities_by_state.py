#!/usr/bin/python3
"""Module listing all cities from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    curs = connexion.cursor()
    curs.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """)
    rows = curs.fetchall()

    for row in rows:
        print(row)
    curs.close()
    connexion.close()
