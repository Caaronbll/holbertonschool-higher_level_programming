#!/usr/bin/python3
"""script that takes in the name of a state as an
    argument and lists all cities of that state"""

import sys
import MySQLdb

if __name__ == "__main__":
    """documentation"""

    db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")

    db_connect = db_cnctn.cursor()
    db_connect.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    print(", ".join([row[2] for row in
                     db_connect.fetchall() if row[4] == sys.argv[4]]))
