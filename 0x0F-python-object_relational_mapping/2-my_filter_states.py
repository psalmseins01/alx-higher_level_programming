#!/usr/bin/python3
"""Lists out the states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn_db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn_db.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cur.execute(query)
    get_rows = cur.fetchall()
    for row in get_rows:
        print(row)
    cur.close()
    conn_db.close()
