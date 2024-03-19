#!/usr/bin/python3
"""liste tous les objets qui contiennent
   la lettre 'a' dans le nom de l'état
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
    states_with_a = session\
        .query(State)\
        .order_by(State.id)\
        .filter(State.name.like("%a%"))

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
