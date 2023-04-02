"""
Description: The file containing the SQLAlchemy declarative base and database connection setup.
"""

## -- 3rd Party Imports -- ##

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

## -- Project Imports -- ##

from app.config import settings

## -- Declarative Base -- ##

Base = declarative_base()

## -- Database Connection Setup -- ##

url = URL.create(
    drivername=settings.DATABASE_DRIVERNAME,
    username=settings.DATABASE_USERNAME,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    database=settings.DATABASE_NAME,
    port=int(settings.DATABASE_PORT)
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = Base.metadata

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()