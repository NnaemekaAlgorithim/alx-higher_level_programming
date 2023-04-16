#!/usr/bin/python3
"""
Prints all states that starts with N(upper N)
"""

import sys
import MySQLdb

if __name__ == '__main__':
    data_base = MySQLdb.connect(
               user=sys.argv[1],
               passwd=sys.argv[2],
               db=sys.argv[3],
               port=3306,
               host='localhost')
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
