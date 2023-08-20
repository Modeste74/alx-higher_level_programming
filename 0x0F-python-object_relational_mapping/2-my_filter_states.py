#!/usr/bin/python3
"""defines a function list_state"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    db.close()
