#!/usr/bin/python3
"""defines a function cities_by_state"""

import MySQLdb
import sys


def cities_by_state(username, password, database):
    """lists all cities from the database
    hbtn_0e_4_usa"""
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        cursor.execute(
                "SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id")
        cities = cursor.fetchall()
        for city in cities:
            print(city)
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

    cities_by_state(username, password, database)
