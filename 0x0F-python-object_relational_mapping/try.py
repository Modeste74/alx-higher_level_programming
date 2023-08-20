#!/usr/bin/python3
"""defines a function list_state"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cursor.execute(query, (sys.argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
