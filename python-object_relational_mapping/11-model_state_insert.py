#!/usr/bin/python3
"""Add a state
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

    "crée une nouvelle instance de la classe State"
    "Cette ligne ne l'ajoute pas encore à la base de données"
    new = State(name="Louisiana")

    "ajoute à la session SQLAlchemy"
    "sera enregistrée dans la base de données"
    "lorsqu'une transaction sera validée"
    session.add(new)

    "commit() pour valider la transaction"
    session.commit()

    print(new.id)
    session.close()
