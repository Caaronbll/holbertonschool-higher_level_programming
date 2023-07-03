#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state"""

import sys
import MySQLdb

if __name__ == "__main__":
    """documentation"""

    db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")

    db_connect = db_cnctn.cursor()
    db_connect.execute("SELECT cities.name FROM cities\
                JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s ORDER BY cities.id ASC")

    for row in db_connect.fetchall():
        print(f"{row}")
