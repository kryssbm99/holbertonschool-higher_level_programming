#!/usr/bin/python3
"""
Module to list all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_all_states(username, password, dbname):
    """
    Connects to the database and lists all State objects,
    sorted by states.id in ascending order.
    """
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, dbname), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print each state
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_all_states(username, password, dbname)
