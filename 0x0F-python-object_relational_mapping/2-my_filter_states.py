#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'

    db = MySQLdb.connect(host=host, user=mysql_username, passwd=mysql_password,
                         db=database_name, port=3306)

    cursor = db.cursor()
    query = 'SELECT * FROM states WHERE name LIKE BINARY "{}"\
 ORDER BY id ASC'.format(sys.argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
