#!/usr/bin/python3
"""
Module to print the State object with the name passed as argument
from the database hbtn_0e_6_usa, safe from SQL injection.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name(username, password, dbname, state_name):
    """
    Connects to the database and prints the State object with the
    given name, displaying the state's id. If not found, prints 'Not found'.
    """
    # Create an engine that connects to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, dbname),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the state's id or 'Not found'
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        get_state_by_name(username, password, dbname, state_name)
