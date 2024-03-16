#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import mysql.connector
import sys

if __name__ == '__main__':
    db = mysql.connector.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()