#!/usr/bin/python3
"""contains a sub-class City
that inherits from Base"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """defines a City"""
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True,
            nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer, ForeignKey('states.id'),
            nullable=False)
