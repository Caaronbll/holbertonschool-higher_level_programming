#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states"""


import sys
import MySQLdb

if __name__ == "__main__":
    """main function"""

    db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")

    db_connect = db_cnctn.cursor()
    db_connect.execute("SELECT * \
                 FROM `states` ")