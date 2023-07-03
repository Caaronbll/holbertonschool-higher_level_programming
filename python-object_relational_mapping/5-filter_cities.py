#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state"""

import sys
import MySQLdb

if __name__ == "__main__":
    """documentation"""

    db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")

    cursor = db_cnctn.cursor()

    buffer_string = "SELECT cities.name FROM cities\
                JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s ORDER BY cities.id ASC"

    cursor.execute(buffer_string, (sys.argv[4],))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print()

    for i in range(len(rows) - 1):
        print(rows[i][0], end=', ')
    print(rows[len(rows) - 1][0])
