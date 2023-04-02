"""
Description: The file containing FastAPI routes for resource1.
"""

## -- 3rd Party Imports -- ##

from fastapi import APIRouter, Request, Depends, Response

## -- Project Imports -- ##

from app.database.base import get_db
from .operations import (get_all_resource1, create_resource1)
from .schemas import (Resource1)

## -- Init Router -- ##
router = APIRouter()

## -- Add Routes To Router -- ##

# GET /resource1
@router.get("/resource1")
async def list_all_resource1(response: Response, db=Depends(get_db)):

    return get_all_resource1(db)

# POST /resource1
@router.post("/resource1")
async def create_resource1(request: Request, resource1: Resource1, db=Depends(get_db)):

    return create_resource1(db, resource1)