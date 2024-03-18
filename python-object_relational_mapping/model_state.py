#!/usr/bin/python3
"""Définition de la classe State associée à la table states
   dans une base de données MySQL."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Classe State."""
    'nom de la table'
    __tablename__ = 'states'
    
    'colonnes de la table'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
