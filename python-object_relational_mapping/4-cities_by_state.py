#!/usr/bin/python3
"""
Module to list all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities(username, password, dbname):
    """
    Connects to the database and prints all cities sorted by id.
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
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    # Fetch all the results
    cities = cursor.fetchall()

    # Print each city
    for city in cities:
        print(f"({city[0]}, '{city[1]}', '{city[2]}')")

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_cities(username, password, dbname)
