from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Taxes(Base):
    __tablename__ = "taxes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    year = Column(Integer)
    salary_income = Column(Integer)
    salary_hours = Column(Integer)
