#!/usr/bin/python3
"""list all states in the table"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{db_username}:{db_password}"
            "@localhost:3306/{db_database}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
