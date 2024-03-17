#!/usr/bin/python3
"""
This module lists the table.
"""
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for rez in (session.query(State.name, City.id, City.name)
                     .filter(City.state_id == State.id)):
        print(rez[0] + ": (" + str(rez[1]) + ") " + rez[2])
