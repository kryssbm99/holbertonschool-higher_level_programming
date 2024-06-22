#!/usr/bin/python3
"""
Module to list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

def list_states(username, password, dbname):
    """
    Connects to the database and prints all states sorted by id.
    """
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(f"({state[0]}, '{state[1]}')")

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
    else:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
