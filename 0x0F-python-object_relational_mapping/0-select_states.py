#!/usr/bin/python3
# import the DB and list states

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_Name = sys.argv[3]

    DB = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=username,
                        passwd=password,
                        db=DB_Name,
                        chartset="utf8")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    DB.close()
