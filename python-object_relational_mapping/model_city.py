#!/usr/bin/python3
"""Définition de la classe City associée à la table cities
   dans une base de données MySQL."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Classe City"""
    'nom de la table'
    __tablename__ = 'cities'

    'colonnes de la table'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
