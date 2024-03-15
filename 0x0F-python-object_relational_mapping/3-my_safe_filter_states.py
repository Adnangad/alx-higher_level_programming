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
    search = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    cur.execute(query, (search,))
    rez = cur.fetchall()
    for i in rez:
        print(f"{i}")
    cur.close()
    db.close()
