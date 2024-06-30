#!/usr/bin/python3
"""
 a script that takes in the name of
 a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa
 """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connect = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_connect.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN \
            states ON cities.state_id = states.id \
            where states.name LIKE %s ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
