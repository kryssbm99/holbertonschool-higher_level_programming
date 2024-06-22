#!/usr/bin/python3
"""
Module to add the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana(username, password, dbname):
    """
    Connects to the database and adds the State object "Louisiana",
    then prints the new state's id.
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

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new state to the session
    session.add(new_state)

    # Commit the transaction to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        add_louisiana(username, password, dbname)
