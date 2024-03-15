#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    try:
        connection = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
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
