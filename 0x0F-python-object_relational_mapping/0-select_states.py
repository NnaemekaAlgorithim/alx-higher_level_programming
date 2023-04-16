#!/usr/bin/python3
"""
Prints all states from the database hbtn_0e_0_usa
and take user, password and database name as arguments
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
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')

    states = cursor.fetchall()
    for state in states:
        print(state)
