#!/usr/bin/python3
"""Deletes the state containing
the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ = "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{db_username}:{db_password}"
            "@localhost:3306/{db_database}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_del = session.query(State).filter(
            State.name.like("a%")).all()
    for state in state_to_del:
        session.delete(state)
    session.commit()
    session.close()
