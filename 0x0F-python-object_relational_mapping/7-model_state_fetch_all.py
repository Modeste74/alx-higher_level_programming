#!/usr/bin/python3
"""list all states in the table"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
            "@localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
