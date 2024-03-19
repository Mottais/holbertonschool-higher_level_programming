#!/usr/bin/python3
"""Imprime le premier objet State (de la table states)
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
    state_furst_id = session\
        .query(State)\
        .order_by(State.id)\
        .first()
    if state_furst_id:
        print("{}: {}".format(state_furst_id.id, state_furst_id.name))
    else:
        print('Nothing')

    session.close()
