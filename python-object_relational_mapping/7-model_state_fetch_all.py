#!/usr/bin/python3
"""Liste de tous les États par ordre croissant de id
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session\
            .query(State)\
            .order_by(State.id)\
            .all():
        print("{}: {}".format(state.id, state.name))
    session.close()
