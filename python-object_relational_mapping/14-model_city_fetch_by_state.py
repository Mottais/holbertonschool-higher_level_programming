#!/usr/bin/python3
"""Module joining 2 tables"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    Query_cities_states = session\
        .query(State, City)\
        .join(City)\
        .order_by(City.id.asc())

    for state, city in Query_cities_states.all():
        print(state.name + ': (' + str(city.id) + ') ' + city.name)

    session.close()
