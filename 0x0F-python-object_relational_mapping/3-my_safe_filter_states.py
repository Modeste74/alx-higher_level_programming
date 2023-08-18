#!/usr/bin/python3
"""defines a function list_state"""

import MySQLdb
import sys


def list_state(username, password, database, state_name):
    """displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    This script is safe from SQL injections"""
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        if states:
            for state in states:
                print(state)
        else:
            print("State not found")
        db.close()
    except MySQLdb.Error as e:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_state(username, password, database, state_name)
