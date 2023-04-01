from fastapi import APIRouter, Depends
from app.database.base import get_db
from .operations import (get_taxes, post_taxes)
from .schemas import (Taxes)

router = APIRouter()

@router.get("/taxes_declarations")
async def list_declarations(db=Depends(get_db)):
    """
    Get all declarations
    """
    taxes = get_taxes(db)
    
    return taxes

@router.post("/taxes_declarations")
async def create_taxes(taxes: Taxes, db=Depends(get_db)):
    """
    Create declarations
    """
    return post_taxes(db, taxes)