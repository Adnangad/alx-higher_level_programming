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
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))
    rez = cur.fetchall()
    for j, i in enumerate(rez):
        if j < len(rez) - 1:
            print(i[0], end=', ')
        else:
            print(i[0])
    cur.close()
    db.close()
