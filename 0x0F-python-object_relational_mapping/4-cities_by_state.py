#!/usr/bin/python3
'''
script that prints all cities from the database
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
    cursor.execute('SELECT cities.id,\
        cities.name, states.name FROM cities JOIN states\
        ON cities.state_id = states.id;')

    states = cursor.fetchall()

    for state in states:
        print(state)
