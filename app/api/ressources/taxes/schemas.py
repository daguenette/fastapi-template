from pydantic import BaseModel

class Taxes(BaseModel):
    email: str
    name: str
    year: int
    salary_income: int
    salary_hours: int