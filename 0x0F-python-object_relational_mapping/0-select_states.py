#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cr = db.cursor()  # Changed from cur to cr
    cr.execute("SELECT * FROM states")
    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()  # Changed from cur to cr
    db.close()

