#!/usr/bin/python3
"""
Module to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, dbname):
    """
    Connects to the database and deletes all State objects with a name
    containing the letter 'a'.
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

    # Query all State objects with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state
    for state in states:
        session.delete(state)

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        delete_states_with_a(username, password, dbname)
