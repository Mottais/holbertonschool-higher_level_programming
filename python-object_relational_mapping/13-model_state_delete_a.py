#!/usr/bin/python3
"""Supprime tous les États contenant la lettre 'a'
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
    Query_state_contient_a = session\
        .query(State)\
        .filter(State.name.like('%a%'))

    for state in Query_state_contient_a.all():
        session.delete(state)

    session.commit()
    session.close()
