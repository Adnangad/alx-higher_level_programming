#!/usr/bin/python3
"""
This module lists the table.
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).limit(1).all()
    for i in data:
        if i is None or i == '':
            print("Nothing")
        print(f"{i.id}: {i.name}")
