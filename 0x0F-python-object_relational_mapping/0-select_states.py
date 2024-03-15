#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
    rez = cursor.fetchall()
    for i in rez:
        print(f"{i}")
    cursor.close()
    connection.close()
