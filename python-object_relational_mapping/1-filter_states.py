#!/usr/bin/python3
"""script that lists all states with a name starting with N"""

import sys
import MySQLdb

if __name__ == "__main__":
    """documentation"""
    db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
    cur = db_cnctn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    for row in cur.fetchall():
        print("{}".format(row))

    cur.close()
    db_cnctn.close()
