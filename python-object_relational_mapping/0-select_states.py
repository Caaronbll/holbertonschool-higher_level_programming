#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb


if __name__ == "__main__":
    """main function"""

    db_cnctn = MySQLdb.connect(host="localhost", port="3306",
                               usermane=sys.argv[1], password=sys.argv[2],
                               database=sys.argv[3],
                               charset="utf8")

    db_connect = db_cnctn.cursor()
    db_connect.execute("SELECT * FROM states ORDER BY id ASC")

    for row in db_connect.fetchall():
        print(f"{row}")
