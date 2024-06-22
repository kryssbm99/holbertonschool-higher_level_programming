#!/usr/bin/python3
"""
Module to change the name of a State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, dbname):
    """
    Connects to the database and changes the name of the State object
    with id = 2 to "New Mexico".
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

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the state's name if found
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        update_state_name(username, password, dbname)
