#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
md = MetaData()
Base = declarative_base(metadata=md)
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
