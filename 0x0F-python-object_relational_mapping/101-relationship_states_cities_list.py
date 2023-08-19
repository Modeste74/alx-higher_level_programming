#!/usr/bin/python3
"""lists all State objects, and corresponding
City objects, contained in the database
hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{db_username}:{db_password}"
            "@localhost:3306/{db_database}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for stAte in states:
        print(f"{stAte.id}: {stAte.name}")
        for city in state.cities:
            print(f"{city.id}: {city.name}")
    session.close()
