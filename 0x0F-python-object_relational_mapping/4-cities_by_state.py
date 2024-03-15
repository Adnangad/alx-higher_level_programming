#!/usr/bin/python3
"""
lists the states in a table.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON state_id = states.id ORDER BY cities.id ASC")
    rez = cur.fetchall()
    for i in rez:
        print(f"{i}")
    cur.close()
    db.close()
