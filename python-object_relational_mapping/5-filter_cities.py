#!/usr/bin/python3
"""
Module to list all cities of a given state from the database hbtn_0e_4_usa,
safe from SQL injection.
"""
import MySQLdb
import sys


def list_cities_by_state(username, password, dbname, state_name):
    """
    Connects to the database and prints all cities of a given state,
    sorted by cities.id. This function is safe from SQL injection.
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

    # Execute the SQL query using parameterized queries
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Print each city
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_by_state(username, password, dbname, state_name)
