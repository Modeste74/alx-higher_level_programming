#!/usr/bin/python3
"""list all state starting with
the letter 'N'"""

import MySQLdb
import sys


def list_by_name(username, password, database):
    """defines a function to list states
    starting with 'N'"""
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_by_name(username, password, database)
