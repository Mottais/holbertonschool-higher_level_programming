#!/usr/bin/python3
"""Change le nom d'un État qui a id = 2 à 'New Mexico'
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
    Query_id_2 = session\
        .query(State)\
        .filter(State.id == 2)

    if Query_id_2.count() > 0:
        Query_id_2[0].name = 'New Mexico'
    session.commit()
    session.close()
