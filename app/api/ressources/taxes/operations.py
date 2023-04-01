from sqlalchemy.orm import Session
import typing as t

from . import models, schemas

# GET Resource (Taxes)
def get_taxes(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.Taxes]:
    
    return db.query(models.Taxes).offset(skip).limit(limit).all()

# POST Resource (Taxes)
def post_taxes(db: Session, taxes: schemas.Taxes):

    db_taxes= models.Taxes(
        email=taxes.email,
        name = taxes.name,
        year = taxes.year,
        salary_income = taxes.salary_income,
        salary_hours = taxes.salary_hours
    )

    db.add(db_taxes)
    db.commit()
    db.refresh(db_taxes)

    return db_taxes