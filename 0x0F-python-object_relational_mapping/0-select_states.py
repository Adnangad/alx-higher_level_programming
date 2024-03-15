#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    try:
        username, password, database = sys.argv[1:]
    except ValuError:
        sys.exit(1)
    try:
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
    except MySQLdb.Error as e:
        print(e)
        sys.exit(1)
    finally:
        cursor.close()
        connection.close()
