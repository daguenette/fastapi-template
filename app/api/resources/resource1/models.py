"""
Description: The file containing SQLAlchemy models for resource1.
"""

## -- 3rd Party Imports -- ##
from sqlalchemy import Column, Integer, String

## -- Project Imports -- ##
from app.database.base import Base

## -- SQLAlchemy Model -- ##
class Resource1(Base):
    __tablename__ = "example_resource1"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String)
    year = Column(Integer)

