#!/usr/bin/python3
"""prints all cities"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{db_username}:{db_password}\
                    @localhost:3306/{db_database}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(
            City, State.id == City.state_id).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
