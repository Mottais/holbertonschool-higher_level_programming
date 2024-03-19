#!/usr/bin/python3
"""imprime l'Id de l'état passé en argument
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
    state_cherché = session\
        .query(State)\
        .filter(State.name.like(argv[4]))

    if state_cherché.count() > 0:
        print(state_cherché[0].id)
    else:
        print('Not found')
    session.close()
