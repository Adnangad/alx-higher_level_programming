#!/usr/bin/python3
import MySQLdb
connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='',
        passwd='',
        db='hbtn_0e_0_usa'
        )
cursor = connection.cursor()
cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
rez = cursor.fetchall()
for i in rez:
    print(f"{i}")
cursor.close()
connection.close()
