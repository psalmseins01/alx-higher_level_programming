#!/usr/bin/python3
"""Lists out the cities"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn_db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn_db.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC")
    get_rows = cur.fetchall()
    for row in get_rows:
        print(row)
    cur.close()
    conn.close()
