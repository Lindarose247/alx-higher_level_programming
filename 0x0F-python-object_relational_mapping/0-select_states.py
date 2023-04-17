#!/usr/bin/python3
"""
This function lists all states from the database hbtn_0e_0_usa.
    
    Parameters:
    username (str): The MySQL username
    password (str): The MySQL password
    database (str): The MySQL database name
    
    Returns:
    None
"""
import sys
import MySQLdb


def list_states():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    query = "SELECT id,name FROM states ORDER by id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()


if __name__ == "__list_states__":
    list_states()
