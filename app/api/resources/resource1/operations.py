"""
Description: The file containing the crud operations for resource1.
"""

## -- 3rd Party Imports -- ##
from sqlalchemy.orm import Session
import typing as t

## -- Project Imports -- ##
from . import models, schemas


## -- Crud Operations -- ##

# Read all entries of resource 1
def get_all_resource1(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.Resource1]:
    
    return db.query(models.Resource1).offset(skip).limit(limit).all()

# Create new entry for resource 1
def create_resource1(db: Session, resource1: schemas.Resource1):

    db_resource1 = models.Resource1(
        name = resource1.name,
        email = resource1.email,
        year = resource1.year,
    )

    db.add(db_resource1)
    db.commit()
    db.refresh(db_resource1)

    return db_resource1