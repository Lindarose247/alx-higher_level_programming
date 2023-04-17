#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb


def states_starting_with_n():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        if r[1][0] == 'N':
            print(r)
    cur.close()
    conn.close()


if __name__ == "_states_starting_with_n_":
    main()
