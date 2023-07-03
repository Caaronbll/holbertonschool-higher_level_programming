#!/usr/bin/python3
"""script that lists all states with a name starting with N"""


import sys
import MySQLdb

if __name__ == "__main__":
    """main function"""

    db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")

    db_connect = db_cnctn.cursor()
    db_connect.execute("SELECT * FROM states WHERE NAME LIKE 'N%'\
                       ORDER BY states.id ASC;")

    for row in db_connect.fetchall():
        print(row)
