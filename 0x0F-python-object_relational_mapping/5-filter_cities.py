#!/usr/bin/python3
"""defines a function filter_cities"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """takes in the name of a state as an argument
    and lists all cities of that state, using
    the database hbtn_0e_4_usa"""
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        query = (
                "SELECT cities.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id")
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
        city_names = ', '.join([city[0] for city in cities])
        print(city_names)
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong Usage")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(username, password, database, state_name)
