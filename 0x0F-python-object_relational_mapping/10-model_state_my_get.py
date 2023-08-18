#!/usr/bin/python3
"""prints the state passed as
an argument from the table given"""

import sys
from sqlalchemy import create_table
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine(
            f"mysql+mysqldb://{db_username}:{db_password}"
            "@localhost:3306/{db_database}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
            State.name == state_name)first()
    if state is None:
        print("Not found")
    else:
        print("{:s}".format(State.id))
    session.close()