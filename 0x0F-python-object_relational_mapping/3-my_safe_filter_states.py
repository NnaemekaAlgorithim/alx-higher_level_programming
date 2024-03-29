#!/usr/bin/python3
'''
script that takes in an argument and displays all values in the states
and is safe from sql injection
'''

import MySQLdb
import sys

if __name__ == '__main__':
    data_base = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    cursor = data_base.cursor()
    cursor.execute('SELECT * from states WHERE name = %s ORDER BY states.id',
                   (sys.argv[4], ))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    data_base.close()
